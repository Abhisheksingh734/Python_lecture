
list=[]
with open("08_files/readlines.txt","r") as f:
    for i in f.readlines():
        i=i.rstrip()
        list.append(i)
        


print(list)