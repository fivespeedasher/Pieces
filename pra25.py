# 求1+2!+3!+...+20!的和。
# Sum=[]
# for i in range (1,21):
#     j=1
#     for k in range(1,i+1):
#        j*=k
#     Sum.append(j)
# print(sum(Sum))

# TODO 使用map
l = range(1,21)
def single(n):
    r = 1
    for i in range(1,n+1):
        r *= i
    return r
print(sum(map(single, l)))