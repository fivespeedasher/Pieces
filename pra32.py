# 按相反的顺序输出列表的值。
# s = input("remember input some empty sys")
# s = s.replace(' ','\n')
# s = s.split('\n')
# row = len(s)
# def handstand(s,row):
#     if row == 0:
#         return s[0]
#     else:
#         print(s[row-1],end='')
#         handstand(s,row-1)
# print(handstand(s,row))

a = ['one', 'two', 'three','four','five']
# for i in a[4::-1]:   #TODO [::-1]顺序取相反操作,1是指隔着一个数
#     print(i)

a.reverse()
print(a)