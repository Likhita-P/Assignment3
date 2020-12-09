tuple=(2,3,4,5,6,7,8)
ans=[]

for i in range(0,4):
    a=tuple[i]
    b=tuple[i+1]
    c=tuple[i+2]
    d=tuple[i+3]
    l=list((a,b,c,d))
    ans.append(l)

print(ans)