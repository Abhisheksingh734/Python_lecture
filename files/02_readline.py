f=open("files/sample.txt","r")

#reads first line
data=f.readline()
print(data)

#reads second line
data=f.readline()  
print(data)

#reads third line...and so on...
data=f.readline()
print(data)

data=f.readline()
print(data)

data=f.readline()
print(data)

f.close()