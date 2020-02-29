# import datetime
# a=datetime.datetime.now()
# print(a)
# print(type(a))
# b=a.strftime('%Y-%m-%d  %H:%M:%S')
# print(b)
# c=a.strftime('%c')
# print(c)
# d=datetime.time()
# print(d)
# print(type(d))

# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
# 创建日期对象
# 日期算术运算
# 日期替换
import datetime
d_time=datetime.datetime.now()
today_time=d_time.strftime('%d-%m-%Y')
print(today_time)

mybirthday=datetime.datetime(year=1998,month=6,day=21)
print(mybirthday.strftime('%d-%m-%Y %Z'))

def getday(n):
    begin_day=mybirthday
    result_day=begin_day+datetime.timedelta(days=n)
    result=result_day.strftime('%d-%m-%Y')
    return result
print(getday(-31))

def change(n=1998,y=6,r=21):
    begin_day=mybirthday
    result_day=begin_day.replace(year=n,month=y,day=r)
    result=result_day.strftime('%d-%m-%Y')
    return result
print(change(1998,r=10))