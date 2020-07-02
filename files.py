# files can be of three types 
# "r" read mode , "w" wrote mode , "a" append mode

* read mode
* read whole file at a time

file = open("file.txt")
var = file.read()
# read 10 characters
print(file.read(10))
print(var)

* To read line by line and create a list out of it

list = file.readlines()
for l in list:
	print(l)
	



# dont forget to close the file 
file.close()
