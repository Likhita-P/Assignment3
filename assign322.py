tuple=('x','y','z')
count=1
list=[]
while(count<5):
    for i in tuple:
        list.append(i*count)
    count+=1
print(list)