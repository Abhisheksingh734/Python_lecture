# print this ---
'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * * 
* * 
* 
'''
n = int(input("Enter:  "))
for row in range(1,2*n):
    if row>n:
        cols = 2*n -row
        for col in range(cols):
            print("* ",end="")
    else:
        cols = row
        for col in range(cols):
            print("* ",end="")
    print("")