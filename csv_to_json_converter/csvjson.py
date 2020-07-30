import csv,json

csv_file_path="Email Attribute to be removed.csv"
json_file_path="email_to_be_synced.json"


# Read csv file and add to data

data = []

with open(csv_file_path) as csv_file:
	csv_reader = csv.DictReader(csv_file,delimiter='|')

	for rows in csv_reader:
		# print(rows,"\n\n\n\n\n\n\n")
		# breakpoint()
		json_data={}
		id = rows['member_id']
		json_data['member_id']=id
		data.append(json_data)


# create new json file and write data on it
with open(json_file_path,'w') as json_file:
	# Make it readable and pretty
	json_file.write(json.dumps(data,indent=4))