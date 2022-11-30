# l1=[1,2,3]
# l2=["a","b","c"]

# new=list(zip(l1,l2))
# print(new)

# z1,z2=zip(*new)
# print(z1,z2)
# # print(list(map(list,zip(*new))))

data=[34,5,67,78,3546,34645,6345,65,54,6,5436,56]
# for idx, num in enumerate(data,start=2):
#     print(list(map(int,(idx,num))))

l=[list((idx,num)) for idx,num in enumerate(data)]
print(l)


