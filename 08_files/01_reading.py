# import os
# print(os.getcwd())


f = open("files/sample.txt","r")
data=f.read()
# data=f.read(5) reads upto 5 charachters
print(data)
f.close()

