mydict = {
    "Name": "Abhishek",
    "Age": "19",
    "Package": "80 LPA",
    "anotherDict": {'Abhishek': 'Player'},
    1:2
}

print(mydict["Name"])
print(mydict["Age"])
print(mydict["Package"])
print(mydict[1])

# Nested Dictionary
print(mydict["anotherDict"]["Abhishek"])

print(list(mydict)) #print KEYS of dictionaries
print(list(mydict.values())) #print values of Dictionary
print((mydict.keys()))
print(mydict.items())
print(mydict.get("Abhishek")) #checks in dictionary returns NONE if not

