# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
# import math
# from functools import reduce
# list = [1]
# for i in range (1,1001):
#     a=i
#     j=1
#     k=2
#     if a%k==0:
#         list.append(k)
#         a=a/k
#         k=2
#         if a==1:
#             if i==sum(list):
#                 print('%d是因数'%i,list)
#                 list=[1]
#                 break




from sys import stdout
for i in range(2,1001):
    k=[]
    n=-1
    s=i
    for j in range(1, i):
        if i%j==0:
            k.append(j)
            n+=1
            s-=j
    if s == 0:
        print(i)
        for a in range(n):
            stdout.write(str(k[a]))
            stdout.write('  ')
        print(k[n])

