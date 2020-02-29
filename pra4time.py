#题目：输入某年某月某日，判断这一天是这一年的第几天？
'''
import time
print(time.asctime(time.localtime(time.time())))
i=int(time.time())
d=int(i/60/60/24)
print(d)
#其他的输出时间方式
#import time
#t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
#t = time.mktime(t)
#print(time.strftime('%Y %m %d %H:%M:%S'),time.gmtime(t))
'''
year=int(input('year'))
mon=int(input('mon'))
day=int(input('day'))
sum=0

if year%4==0:
    arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    arr = [31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for md in range(1, 13):
    if mon>md:
        sum+=arr[md]
sum+=day
print('It is %dth day'%sum)