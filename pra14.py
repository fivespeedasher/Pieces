# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

# i=int(input('enter a num'))
#
# a=i
# for k in range(2,i):
#     for j in range(2,i):
#         if a%j==0:
#             print(j)
#             a=a/j
#             break
#     if a==1:
#         break


import math

number=int(input('enter a number'))

list=[]

def factor(num):
    # if not isinstance(number, int) or number <= 0:
    #     print('请输入正确的数字')
    #     exit()
    i = 2

    isZHISHU=True
    rad = int(math.sqrt(num))+1
    while i<=rad:
        if num%i==0:
            list.append(i)
            isZHISHU=False
            factor(num/i)
            i+=1
            break
        i+=1
    if isZHISHU:
        list.append(num)

factor(number)
print(list)



# def reduceNum(n):
#     print('{} = '.format(n),)
#     if not isinstance(n, int) or n <= 0:
#         print('请输入一个正确的数字 !')
#         exit(0)
#     elif n in [1]:
#         print('{}'.format(n))
#     while n not in [1]:  # 循环保证递归
#         for index in range(2, n + 1):
#             if n % index == 0:
#                 n /= index  # n 等于 n/index
#                 n=int(n)
#                 if n == 1:
#                     print(index)
#                 else:  # index 一定是素数
#                     print('{} *'.format(index),)
#                 break
#
#
# reduceNum(90)
# reduceNum(100)