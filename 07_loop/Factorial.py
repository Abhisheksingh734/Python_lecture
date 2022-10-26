from re import I


num=int(input())
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact,f"The factorial of this number is {fact}")