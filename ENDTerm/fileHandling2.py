import os
def count_lines(file_name):
    with open(file_name) as f:
        return len(f.readlines())

def mover_cursor(file_name,pos):
    with open(file_name) as f:
        f.seek(pos)
        return f.read()
file_name="primary.txt"
# n=int(input())
# print(mover_cursor(file_name,n))

def copy(file_name,copyto):
    with open(file_name) as f1:
        with open("secondary.txt","w") as f2:
            f2.write(f1.read())
        with open("secondary.txt") as f3:
            print(f3.read().upper())

copy(file_name,"secondary.txt")

if os.path.exists("secondary.txt"):
    os.remove("secondary.txt")
else:
    print("no file found....")

