# 利用递归方法求5!。 递归公式：fn=n*f(n-1)
def pong(n):
    if n==1:
        return n
    else:
        return n*pong(n-1)
print(pong(5))