def isPalindrome(num):
    return int(str(num)[::-1])==num

def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True


digit=int(input("Enter digit "))
# for i in range(10**digit,-1):
if 2<=digit<10:

    for i in reversed(range(10**digit)):
        if isPalindrome(i) and isPrime(i):
            print(i)
            break
else:
    print("Invalid")