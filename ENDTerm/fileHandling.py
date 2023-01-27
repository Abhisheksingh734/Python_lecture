def countLines():
    with open("Data.txt","r") as f:
        return len(f.readlines())

def countWords():
    with open("Data.txt","r") as f:
        return len(f.read().split())

def countCharac():
    with open("Data.txt","r") as f:
        return len(f.read())

def reverseLine(file_name):
    with open(file_name,"r") as f:
        for i in f.readlines():
            print(i[::-1])
file_name="Data.txt"

reverseLine(file_name)


