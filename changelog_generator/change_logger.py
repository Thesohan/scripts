import sys
commits=list(sys.argv[1].split('\n'))

class Commit:

    def __init__(self,jira,type,endpoints,message,des):
        self.type=type
        self.endpoints= endpoints
        self.message = message
        self.des = des

commit_list=[]
for commit in commits:
    # print(commit)
    des = commit.split(':')
    try:
        commit_list.append(Commit(jira=des[0],type=des[1],endpoints=des[2],message=des[3],des=des[4]))
    except Exception as e:
        pass

# print(commit_list[0].jira)
# generating beautiful changelog
full_text=""
for commit in commit_list:
    full_text+="\n"
    full_text +="{} : {}: {}\n\n\t{}".format(commit.type,commit.endpoints,commit.message,commit.des)

file1 = open('myfile.md', 'w')

# Writing a string to file
file1.write(full_text)
file1.close()