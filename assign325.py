tuple=(1,2,3)
count=1
ans=[]
while(count<4):
    for i in tuple:
        l=(i,count)
        ans.append(l)
    count+=1
print(ans)
