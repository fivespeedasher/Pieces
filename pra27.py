# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
def intp(s,n):
    if n==0:
        return ''
    else:
        print(s[n-1],end='')
        return intp(s,n-1)
s = input('enter:')
n = len(s)
print(intp(s,n))

# TODO 为何输出结果会有None？
