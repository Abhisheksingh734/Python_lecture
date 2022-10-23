
#  Print this ->    ***
#                   * *
#                   ***

n=int(input("enter rows: "))

for i in range(n):
    print("*",end="")
    if i==(n//2):
        print(" ",end="")
    else:
        print("*",end="")
    print("*")