#write a program to make a copy of a text file "this.txt"

with open("files/this.txt","r") as f:
    data=f.read()
with open("files/Copythis.txt","w") as f:
    f.write(data)
