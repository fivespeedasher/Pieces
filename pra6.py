# Fn = F[n-1]+ F[n-2](n=>2)
def fib(n):
    if n==0 :
        return [0]
    elif n==1 :
        return [0,1]
    else:
        fibs=[0,1,1]
        for i in range(3,n):
            fibs.append(fibs[-1]+fibs[-2])
        return fibs



# 输出了第10个斐波那契数列
print(fib(8))

# a,b=0,1
# while a<1000:
#     print(a,end=",")
#     a,b=b,a+b