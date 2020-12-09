list=[1,2,3,-5,2,-6]
ans=[]

def func(x):
    if x>0:
        return True
    else:
        return False

def myfilter(func,list):
    for i in list:
        res=func(i)
        if res==True:
            ans.append(i)
    return ans

final=myfilter(func,list)

for x in final:
    print(x)