#finding prime number

num=int(input())
for i in range(2,num):
    if num%i==0:
        print("It is not a prime number")
        break
    else:
        print("It is a prime number")
        break