myString=input("Enter the string: ")
k=int(input())

finalList=[]
for i in range(0,len(myString),k):
    sub_part=myString[i:i+k]
    unique_str=""
    for j in sub_part:
        if j not in unique_str:
            unique_str+=j
    finalList.append(unique_str)
    
print(finalList)


