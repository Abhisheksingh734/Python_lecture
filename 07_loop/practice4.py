nums=[1,2,3,4,5,6,7,8,9]

# newlist=filter(lambda n: n%2==0,nums)
# print(list(newlist))


letter="abcd"
num="1234"


mylist=[(l,n) for l in letter for n in num]
print(mylist)
