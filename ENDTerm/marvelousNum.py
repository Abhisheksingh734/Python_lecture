def ``

count =0
for i in range(r1,r2+1):
    if(i-int(str(i)[::-1]))%k==0:
        count+=1
print(count) 
