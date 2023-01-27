keys=input().split(",")
values=list(map(int,input().split(",")))

myDict=dict(zip(keys,values))
while True:
    search_key=input("enter key to be searched ")
    try:
        print(myDict[search_key])
        break
    except:
        print("key not found")
        