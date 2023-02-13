l1=[1,2,3]
l2=["a","b","c"]

new=list(zip(l1,l2))

z1,z2=zip(*new)
print(z1,z2)
print(new)
# # print(list(map(list,zip(*new))))

# data=[34,5,67,78,3546,34645,6345,65,54,6,5436,56]
# for idx, num in enumerate(data,start=2):
#     print(list(map(int,(idx,num))))

# l=[list((idx,num)) for idx,num in enumerate(data)]
# print(l)


# keys=[1,2,3,4,5]
# values=[5,6,7,8,8]
# myDict=dict(zip(keys,values))
# print(myDict)

myDict={x.upper():x*3 for x in "coding"}
print(myDict)