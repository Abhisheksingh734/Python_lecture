
#  Print this ->    ***
#                   * *
#                   ***

# n=int(input("enter rows: "))

# for i in range(n):
#     print("*",end="")
#     if i==(n//2):
#         print(" ",end="")
#     else:
#         print("*",end="")
#     print("*")






# Increasing triangle pattern

# rows=int(input())
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()





#Decreasing triangle pattern
rows=int(input())
for i in range(rows):
    for j in range(rows-i):
        print("*",end=" ")
    print()
    
