# 判断101-200之间有多少个素数，并输出所有素数。
import math
import sys
h=0
leap=1
for i in range(101,201):
    for j in range(2,i):
        if i%j==0:
            leap=0
            break
    if leap==1:
        h+=1
        print(i)
    leap=1
    # 为什么leap=1 一旦放在if的循环之中for函数运行一次直接跳出？
print(h)
