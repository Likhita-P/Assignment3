def fun(var):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (var in letters):
        return True
    else:
        return False

def filter(function,input):
    list=[]
    for i in input:
        if fun(i)==True:
            list.append(i)
    return list
# sequence
input = ['g','o','o','d','m','o','r','n','i','n','g']

# using filter function
final = filter(fun, input)

print('The filtered letters are:')
for s in final:
    print(s)