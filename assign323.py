tuple=(2,3,4,5,6)
ans=[]

for i in range(0,3):
    a=[tuple[i]]
    b=[tuple[i+1]]
    c=[tuple[i+2]]
    ans.extend((a,b,c))

print(ans)