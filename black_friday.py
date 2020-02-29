'''2018.10.15星期一'''
from datetime import *
import calendar

class Black_Friday():
    def __init__(self,year):
        self.year = year
    def find_it(self):
        print('The black Fridays of year %d is(%d-1-1 is %s)'%(self.year,self.year,datetime(self.year, 1, 1).strftime('%A')))
        l = []
        flag = 0
        for i in range(12):
            if calendar.weekday(self.year,i+1,13) == 4:
                l.append('%s/%s/%s'%(self.year,i+1,13))
                flag=1
        if flag:
            print(l)
        else:
            print('None')
year = int(input('查询年份(1970~9999)'))
Black_Friday(year).find_it()