# files can be of three types 
# "r" read mode , "w" wrote mode , "a" append mode

# * read mode
# * read whole file at a time

file = open("file.txt")
var = file.read()
# read 10 characters
print(file.read(10))
print(var)

#To read line by line and create a list out of it

list = file.readlines()
for l in list:
	print(l)
	
# file.readline() will read upto nuewline and return it then read upton new line
file.readline()


# dont forget to close the file 
file.close()

# Everytime you make a read operation the cursor pointing in file will be moved
# to make this to default sittings 
file.seek(10) # the cursor will move to 10th byte
file.seek(0)

#to open a file save then open it with "with" statkement

with open("file.txt") as file:
	print(file.read())


import json
# JSON
# dumps takes dictionary obj into a string
json.dumps(obj,fileobj) #serialize obj as a json formatted stream of fileobj

# takes json string and return json file
json.loads(data)



# Python Asynchronous
# 1 multi processes -- different process running same programme like two python interpretors
# 2 mutli threading -- one process will managing multiple threadings
# in case of multi threading can share memory but not possible by multi process if you want to achiece sharing memmory between mprocess deadlock will happen
# 3 Coroutines -- giving context to another function
def func2():
	return 3
def func():
	return func2
def main():
	pass
# func will return func2 ..context switching is possible in couroutine
# 4 AsyncIO
# library present in python3.7 



