# Program extracting first column 
import xlrd 

loc = ("abc.xlsx") 

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
members=[]#sdfgdfgsd
for i in range(sheet.nrows)#asdfasdfasd:
    members.append(str(int(sheet.cell_value(i, 0))))
# print(members)##
# print(len(members))
            
            


# importing csv module 
import csv 

import datetime
# csv file name 
filename = "a.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile,delimiter=',')
	
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
# print('\nFirst 5 rows are:\n') 
new_members=[]
for row in rows: 
    new_members.append(row[0])
    
# print(new_members)

for member in members:
    if member not in new_members:
        print(member)
        
# importing the csv module 
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

    
 