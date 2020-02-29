# # 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
import math
i=int(input('How many numbers do you want to puls?'))
a=int(input('What is the base'))
s=0
for j in range (i):
    if j==0:
        p=0
    else :
        k=j
        while(k>0):
            p += pow(10,k)*a
            k-=1
        p+=a
s+=a+p
print('sum=%d'%s)


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
# from functools import reduce
# Tn = 0
# Sn = []
# n = int(input('n = '))
# a = int(input('a = '))
# for count in range(n):
#     Tn = Tn + a
#     a = a * 10
#     Sn.append(Tn)
#     print(Tn)
# sn = reduce(lambda x, y: x + y, Sn) #TODO 这个很好用，数组元素求和
# print("计算和为：", sn)