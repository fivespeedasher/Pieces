# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
g=0
for i in range(1,10):
    g+=100*i
    for j in range(0,10):
        g+=10*j
        for k in range(0,10):
            g+=1*k
            if i**3+j**3+k**3==g  :
                print(g)
            g-=1*k
        g-=10*j
    g=0


# for n in range(100,1000):
#     i = n / 100
#     j = n / 10 % 10
#     k = n % 10
#     if n == i ** 3 + j ** 3 + k ** 3:
#         print (n)