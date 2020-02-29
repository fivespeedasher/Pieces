# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
def number (s,n):
    if n == 0 :
        return ''
    else:
        print(s[n-1],end='')
        return number(s,n-1)
unmatch = True
while unmatch ==True:
    s = input('enter')  #TODO 如何让输入识别是否属于数字。
    n = len(s)
    if 0<n<6:
        unmatch = False
    else :
        print('请输入不多于5位的正整数')
        unmatch=True
print('该输入为{}位数'.format(n))


print(number(s,n))