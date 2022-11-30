try:
    n=int(input("Enter a number: "))
    print(n)
except ValueError as err:
    print(err)
    print("invalid")
except:
    print("invalid")