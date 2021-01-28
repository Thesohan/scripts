clog() {
	local commits=""
#	if [ -z "$3" ]; then
#
#		if [ -z "$1" ]; then
#			commits=$(git log HEAD...$(git describe --tags --abbrev=0) --pretty='* %s' | sort -r | uniq | grep "BL-")
#		else
#			if [ -z "$2" ]; then
#				commits=$(git log HEAD...$1 --pretty='* %s' | sort -r | uniq | grep "BL-")
#			else
#				commits=$(git log $2...$1 --pretty='* %s' | sort -r | uniq | grep "BL-")
#			fi
#		fi
#	else
		commits=$(git log --pretty='* %s' | sort -r | uniq | grep "BL-")
#	fi
	# Make sure BL is separated from comma, colon, period
	commits=${commits//",BL"/", BL"}
	commits=${commits//".BL"/". BL"}
	commits=${commits//":BL"/": BL"}

	# Find unique BL-XXXXXX patterns
	pattern="BL-[0-9]+"
	declare -a local ticket_arr
	for word in $commits;
	do
		[[ $word =~ $pattern ]]
		if [[ ${BASH_REMATCH[0]} ]]
		then
			ticket_arr+=("${BASH_REMATCH[0]}")
		fi
	done
	local sorted_unique_tickets=($(echo "${ticket_arr[@]}" | tr ' ' '\n' | sort -r | uniq | tr '\n' ' '))

	# Replace BL tickets by markdown hyperlinks
#	for ticket in "${sorted_unique_tickets[@]}";
#	do
#		commits=${commits//$ticket/"[$ticket](https://bankofloyal.atlassian.net/browse/$ticket)"}
#	done
	echo "**Changelog**"
#	echo "$commits"
	python change_logger.py "$commits"
}
clog