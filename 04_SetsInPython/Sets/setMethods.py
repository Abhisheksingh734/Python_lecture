#sets are unordered unindexed, immutable , 

# how to make a set 
a=set()
print(type(a))
a.add(4)
'''it will not add duplicate values'''
a.add(5)
a.add(5)
a.add(5)
print(a) 

# a.add([2,4,5])  #cannot add list and dict in set because list is mutable
# a.add((2,4,5))
print(a)

a.remove(5)
print(a)
a.add(8)
a.add(6)
a.add(9)
a.add(2)

print(a)
# a.remove(7) #throws error if not in set
print(a.pop())
print(a)

# a.clear() Empty the set

u=a.union({17,16}) #returns a new set with all items from both the sets
i=a.intersection({1,2,3,4,5,6,7,8}) #returns a new set which contains only items in both sets
print(u)
print(i)





