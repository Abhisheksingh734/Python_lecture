jerseyNum=list(map(int,input().split(" ")))

def multipleOf(num,li):
    count=0
    for i in li:
        if i%num==0:
            count+=1
    return count

d={}
d["2"]=multipleOf(2,jerseyNum)
d["3"]=multipleOf(3,jerseyNum)
d["5"]=multipleOf(5,jerseyNum)
print(d)
