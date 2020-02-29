# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# from functools import reduce
# son = []
# x1 = 1.0
# y1 = 2.0
# for i in range (20):
#     son.append(y1/x1)
#     x1,y1 = y1,y1+x1
# Sum = reduce(lambda x,y:x+y,son)
# print('前二十项和为：',Sum)

# from functools import reduce
# a = 2.0
# b = 1.0
# l = []
# l.append(a / b)
# for n in range(1,20):
#     b,a = a,a + b
#     l.append(a / b)
# print (reduce(lambda x,y: x + y,l))
