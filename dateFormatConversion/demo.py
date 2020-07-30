# importing csv module 
import csv 

import datetime
# csv file name 
filename = "ssl.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile,delimiter='|')
	
	# extracting field names through first row 
	fields = next(csvreader) 

	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

	# get total number of rows 
	print("Total no. of rows: %d"%(csvreader.line_num)) 

# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 

# printing first 5 rows 
print('\nFirst 5 rows are:\n') 
for row in rows[:5]: 
    print(row)
    # row[1]=datetime.datetime.fromisoformat(row[1])
    # row[1]=row[1].replace(tzinfo=datetime.timezone.utc).isoformat()
    # print(row[1])
    # print(row[5])
    # row[5]=datetime.datetime.fromisoformat(row[5])
    # row[5]=row[5].replace(tzinfo=datetime.timezone.utc).isoformat()
    

# # importing the csv module 
# import csv 


# # name of csv file 
# filename = "updated_ssl.csv"

# # writing to csv file 
# with open(filename, 'w') as csvfile: 
# 	# creating a csv writer object 
# 	csvwriter = csv.writer(csvfile) 
	
# 	# writing the fields 
# 	csvwriter.writerow(fields) 
	
# 	# writing the data rows 
# 	csvwriter.writerows(rows)

    
#  