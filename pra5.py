# a,b,c=map(int,input('enter three numbers\n').split(   ))
# arr=[a,b,c]
# arr.sort()
# # 默认list.sort(cmp=None, key=None, reverse=False)
# print(arr)

l=[]
for i in range(3) :
    x=int(input('GIVE ME A NUMBER'))
    l.append(x)
l.sort(reverse=1)
print(l)