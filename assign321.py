#question 2
#[x,xx,xxx,xxxx,y,yy,...]

count=1
str=""
list=[]
tuple=('x','y','z')

str=""
for i in tuple:
    while(count<5):
        str=str+i
        list.append(str)
        count+=1
    str=""
    count=1
print(list)

