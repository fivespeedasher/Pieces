# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
# s = str(input('输入一个回文数'))
# n = len(s)
# m = n//2
# l1=[]
# l2=[]
# for i in range(0,m+1):
#     l1.append(s[i])
# for j in range(1,m+2):
#     l2.append(s[-j])
# if l1==l2:
#     print('Ture')
# else:
#     print('heheh')

a = int(input("请输入一个数字:\n"))
x = str(a)
flag = True
for i in range(len(x)//2):
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print("%d 是一个回文数!" % a)
else:
    print("%d 不是一个回文数!" % a)
