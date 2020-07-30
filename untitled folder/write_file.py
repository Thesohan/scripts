test_obj = open("demofile3.txt", "w")
test_obj.write("sku,points \n")
test_obj.write("123123,111 \n")
test_obj.write("123123123,222 \n")
test_obj.write("12312321,333 \n")
           
test_obj.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
