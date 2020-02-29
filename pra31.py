# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
import time
w=input('Enter a letter for week')
s=time.asctime()
if s[0]==str.upper(w):
    e=input('Enter one more letter')
    if s[1]==str.lower(e):
        print('TRUE')
    else:
        print('wrong')
else:
    print('wrong')