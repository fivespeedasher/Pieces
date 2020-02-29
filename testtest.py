# shoplist=[1,2,3,4]
# mylist=shoplist[:]
# #different to mylist=shoplist
# print(shoplist)
# print(mylist)
# del shoplist[0]
# print(shoplist)
# print(mylist)

# a=1
# b=2
# c=3
# s='{}{}{}'.format(a,b,c)
# print('{}{}{}'.format(a,b,c))
# print(a+b+c)
# print(s)
# print('%d%d%d' % (a,b,c))
# f='%d%d%d' % (a,b,c)
# print(f)


# files = ['D:\I\'M\\usedbypython\\1.txt']
# s=['q',1,'1',True]
# print(s[-1])

# for s in "HelloWorld":
#     if s=="W":
#         continue
#     print(s,end="")


# d ={"大海":"蓝色", "天空":"灰色", "大地":"黑色"}
# print(d.get("大地", "黄色"))
'''
dict.get(key, default=None)
key -- 字典中要查找的键。
default -- 如果指定键的值不存在时，返回该默认值值。
'''

# txt = open("C:\\Users\\asshole\Desktop\\book.txt", "r")
# print(txt)
# txt.close()

# import math
# s=(3**4+5*6**7)/8
# x=math.sqrt(s)
# print('%.3f' % x)

# import jieba
# # s = "中国特色社会主义进入新时代，我国社会主要矛盾已经转化为人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾。"
# # n = len(s)
# # aa = 0
# # ss = jieba.cut(s)
# # l={}
# # for l in ss :
# #     aa+=1
# # m = aa
# # print("中文字符数为{}，中文词语数为{}。".format(n, m))


# print(ord('1'))
# print(chr(50))
# print(type(ord('中')))
# ten = int(0x4DC0)+50
# print(ten)
# print(chr(0b100110111110010))


# import turtle
# d = 0
# for i in range(4):
#     turtle.fd(200)
#     d = d+90
#     turtle.seth(d)


# ten = int(0x4DC0)+50
# two = bin(ten)
# eig = oct(ten)
# sitn = hex(ten)
# a = [two,ten,eig,sitn]
# print("二进制{}、十进制{}、八进制{}、十六进制{}".format(*a))

# st = '我们的共产党(中国共产党)和共产党...'
# s = ''
# b = False
# for ch in st:
#     if ch == '(':
#         break
#     s = s + ch
# for ch in st:
#     if ch == ')':
#         b = True
#     if b and ch != ')':
#         s = s + ch
# print(s)

# import time
# # t = time.gmtime()
# # print(time.strftime("%Y-%m-%d %H:%M:%S",t))


# import turtle
# for i in range(4):  #一个数字
#     turtle.right(90)
#     turtle.circle(50,180)



# # 从1.csv文件中读取考勤数据
# with open("txt\\1.csv","r",encoding = "utf-8") as fo:
#     foR = fo.readlines()
# ls = []
# for line in foR:
#     line = line.replace("\n","")
#     ls.append(line.split(","))
# print(ls)
# # 从name.txt文件中读取所有同学的名单
# with open("txt\\Name.txt","r",encoding = "utf-8") as foName:
#     foNameR = foName.readlines()
# lsAll = []
# for line in foNameR:
#     line = line.replace("\n","")
#     lsAll.append(line)
# print(lsAll)
# #求出第一次缺勤同学的名单
# for l in ls:
#     for i in l:
#         if i in lsAll:
#             lsAll.remove(i)
#
# print("第一次缺勤同学有：",end ="")
# k = len(lsAll)
# for j in range (k):
#     print(lsAll[j],end=' ')


# import jieba
# with open("C:\\Users\\asshole\Downloads\sgld.txt","r",encoding ="utf-8")as f:
#     lssgld = f.readlines()
# n = 0
# for ls in lssgld:
#
#     for i in ls:
#         if i == '人':
#             n+=1
# print('人:%d 次' % n)


# str1 = 'aabbccddeeffgg'
# print(str1[-10:])


# print("二进制{0:b}、十进制{0}、八进制{0:o}、十六进制{0:x}".format(0x4DC0+50))

# # TODO 方差计算
# def mean(numlist):
#     s = 0.0
#     for num in numlist:
#         s = s + num
#     return s/len(numlist)
# def dev(numlist,mean):
#     sdev = 0.0
#     for num in numlist:
#         sdev = sdev + (num - mean)**2
#     return (sdev /(len(numlist)-1) )** 0.5
# #请输入一个列表：
# ls = eval(input(""))0
# print("均方差为：{:.2f}".format(dev(ls,mean(ls))))


# counts = {}
# d = ['hello','hello','hello','hello','hello','hello','hi','hi','hi','hi','h']
# for word in d:
#     # if word in counts:
#     #     counts[word] += 1
#     # else:
#     #     counts[word] = 1
#     counts[word] = counts.get(word, 0)+1  #TODO 用作字典的建立
#     items = list(counts.items())
# print(counts)
# print(items)
# print(counts.keys(),'',counts.values())



# d = {'hello': 2, 'hi': 4, 'interesting': 1, 'love' : 3}
# a = sorted([[v,k] for k, v in d.items()])
# print(a)
# b = {k:v for v,k in a[-2:]}
# print(b)


# ls = []
# for i in range(1,4):
#     fo =  open("txt\\check\\"+str(i) +".csv","r",encoding = "utf-8")
#     for line in fo:
#         line = line.replace("\n","")
#         ls.append(line.split(",")[0])
#     fo.close()
# counts = {}
# for name in ls:
#     counts[name] = counts.get(name,0)+1
# items = list(counts.items())
# print("全勤同学有：",end ="")
# for i in range(1,75,1):
#     word,num = items[i]
#     if num == 4 :
#         print(word,end=',')




# fo = open("txt\\sgldout.txt", "r", encoding="utf-8")
# words = fo.readlines()
# fo.close()
# sym = "；。，“”： "
# DictWords = {}
# s=[]
# for ls in words:
#     if ls[:-1] not in sym:
#         DictWords[ls[:-1]] = DictWords.get(ls[:-1],0)+1
#         L = list(DictWords.items())
#         L.sort(key = lambda s:s[1],reverse=True)
# # f1 = open('sgldstatistics.txt','w',encoding ="utf-8")
#
# for i in range(5):
#     # f1.wirte(L[i][0]+":"+L[i][1])
#     print(L[i][0]+":"+str(L[i][1]))
# # f1.close()



# h,w = eval(input()) # 请输入身高(m)和体重(kg)，逗号隔开:
# print("BMI 是 {:.1f}".format(h/(w**2)))


# s = '1101' # 请输入一个由1和0组成的二进制数字串：
# d = 0
# while s:
#    d = d*2 + (ord(s[0]) -ord('0'))
#    s = s[1:]
# print("转换成十进制数是：{}".format(d))



# import jieba
# s = input("请输入一个中文字符串，包含逗号和句号：")#'我知道我很帅， 我懂，别说。'
# s = s.replace(' ','').replace('。','').replace('，','').replace('！','')
# sr = jieba.cut(s)
# srr = list(sr)
# print('/'.join(sr))
# print("中文字符数为{}。".format(len(s)))
# print("\n中文词语数为{}。".format(len(srr)))

# print('1.显示所有信息\n2.追加信息\n3.删除信息')
# global start
# again = True
# option = [1,2,3]
# while again :
#
#     start = int(input('请输入数字1-3选择功能'))
#
#     if start not in option:
#         again = True
#     else:
#         again = False
#         print('您选择了功能%d' % start)
# with open('txt\\address.txt','r') as f0:
#     f0L = f0.readlines()
#     if start == 1:
#         for i in f0L:
#             print(i)
#     elif start == 2:
#         new_one = input('输入新信息,以逗号隔开')
#         f1 = open('txt\\new_address.txt','w',encoding='utf-8')
#         for i in f0L:
#             f1.write(i)
#         f1.write(new_one)
#         f1.close()
#     else:
#         print('ok')


# fo = 'Chinese: 80,Math:85,English:92, Physical: 81,Art:85,Chemical:88'
# l = fo.split(',')
# s = 0
# n = len(l)
# for k in l:
#     items = k.split(':')
#     s += int(items[1])
# print("总和是：{}，平均值是：{:.2f}".format(s, s / n))




# import jieba
# s = input("请输入一个中文字符串，包含逗号和句号：")
# d1 = {}
# maxc = 0
# list1 = []
# s = s.replace('，','').replace('。','').replace('、','').replace('“','').replace('”','')
# js = jieba.cut(s)
# for i in js :
#     print(i,end='')
#     print('/ ',end = '')
# js = jieba.cut(s)
# jsc = list(js)
# print("\n中文词语数是：{}".format(len(jsc)))
#
# for k in jsc:
#     d1[k] = d1.get(k,0)+1
# # print(d1)
# d2 = sorted(d1.items(),key=lambda x:x[1],reverse=True)
# print(d2)
# for i,j in d1:
#     print(i+':'+str(j))
# for key in d1:
#     print(d1[key])
# def filter_l(data):
#     # 把字典转换成dict_items，循环里面的key和value，满足if条件返回对应的key和value值
#     return {k: v for k, v in data.items() if v == 3}#TODO 字典的筛选

# import re
# picd = {}
# numd = {}
# fi = open("txt\\dir_50.txt",'r')
# for l in fi:
#     l=l.replace('\n','').split('_')
#
#     # print(l)
#     # print(eval(l[0]))
#     if l[0] != '' :
#         lkey,lvalue = l[1][:-4],eval(l[0])
#         lval = []
#         for v in lvalue:
#             if v != '0':
#                 lval.append(v)
#         if lval:
#             lv= ','.join(lval)
#             print("{}:{}".format( lkey,lv))
#             picd[lkey] = lv
# fi.close()
# idd = {}
# for key in picd:
#     ids = picd[key].split(',')
#     for num in ids:
#         idd[num] = idd.get(num,0) +1
#             #print(num,idd[num])
# s = 0
# for key in idd:
#     s += int(idd[key])
#     # print("{}:{}".format(key, idd[key]))
# count = len(idd)
# print("实际参加测试的人数是：",count)
# print("人均被测次数是：{:.1f}".format(s/count))



# line = '<img src="http://image.ngchina.com.cn/2018/0517/20180517061316312.jpg" alt="美国《国家地理》全球摄影大赛中国区">'
# url = line.split('src=')[-1].split('"')[1]
# print(url)


# for i in range(2,1001):
#     summ = 0
#     for k in range(1,i):
#         if i%k == 0:
#             summ += k
#     if  summ == i:
#         print(i)


# for i in range(2,1001):
#     s = i
#     for j in range(1,i):
#         if i%j == 0:
#             s -= j
#     if s == 0:
#         print(i)


# ifilename = input("请输入文件名：\n")
# fp = open(ifilename,'w',encoding='utf-8')
# ch = input("请输入字符串：\n")
# while ch != '@':
#     if '@' in ch:
#         t = ch.find("@")
#         fp.write(ch[0:t])
#         break
#     else:
#         fp.write(ch + " ")
#     ch = input()
# fp.close()

# la = 'python'
# li = 889
# try:
#     s = eval(input('请输入整数：'))
#     ls = s*2
#     print(ls)
# except:
#     print('请输入整数')

# w = input('‘请输入数字和字母构成的字符串：')
# for x in w:
#     if '0'<= x <= '9':
#         continue
#     else:
#         w.replace(x,'')#TODO replace 木有返回值
# print(w)


# import turtle
# edge = 6
# d = 0
# k = 1
# for j in range(1000):
#    for i in range(edge):
#        turtle.fd(k)
#        d += 60
#        turtle.seth(d)
#        k += 1
# turtle.done()

# import sys
# print(sys.version)  #TODO 查询版本


# def getInput():
#     i = input()
#     while type(eval(i)) != type(1):
#         i = input()
#     return i
# print(getInput())


# dic = {'a':1,'b':2}
# dics = dic.items()
# ldic = list(dic)
# for i in dic:
#     print(i)
# print(list(dics)) #todo list可以消去前面的 dic.items(...)

# lists = [1,2,3]
# print(lists)  #todo 列表输出仍为列表


# studs= [{'sid':'103','Chinese': 90,'Math':95,'English':92},{'sid':'101','Chinese': 80,'Math':85,'English':82},{'sid':'102','Chinese': 70,'Math':75,'English':72}]
# scores = {}
# for stud in studs:
#     sv = stud.items()
#     v = []
#     for it in sv:
#         if it[0] =='sid':
#             k = it[1]
#         else:
#             v.append(it[1])
#     scores[k] = v
# so =list(scores.items())
# so.sort(key = lambda x:x[0],reverse = False)   #todo 列表对x[0]排序sort有返回值
# for l in so:
#     print('{}:{}'.format(l[0],l[1]))


# s = "11+5in"
# print(s[1:-2])
# print(eval(s[1:-2]))  # TODO 神奇的eval()


# l = [1,2,1,2,1,1]
# print(l)      # todo 列表元素可以重复

#
# d = {}
# for i in range(26):
#     d[chr(i+ord("a"))] = chr((i+13) % 26 + ord("a"))
# for c in "Python":
#     print(d.get(c, c), end="")


# min = open('命运-网络版.txt','r',encoding='utf-8')
# xun = open('寻梦-网络版.txt','r',encoding='utf-8')
# miny = min.read
# xunm = xun.read()
# dicm = {}
# dicx = {}
# for i in miny:
#     dicm[i] = dicm.get(i,0)+1
# del dicm['\n']
# del dicm[' ']  # todo 文件字频
# min.close()


# import time
# t = time.asctime(time.localtime(time.time()))
# print(t)
# print(time.strftime('%Y %m %d %H:%M:%S',time.gmtime())) #TODO 这里小时有误



# import random
# random.seed(0x1010)
# s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
# a = []
# secs = ''
# j = 0
# while j<10:
#     for k in range(10):
#         secp = random.choice(s)
#         secs += secp
#     if secs[0] not in a:
#         a.append(secs[0])
#         print(secs)
#         j+=1
#     secp = ''
#     secs = ''


# def is_prime(n):
#     for j in range(2, n):
#         if n % j == 0:
#             return True
#     else:
#         return False
#
#         # 此处可为多行函数定义代码
# ls = [23, 45, 78, 87, 11, 67, 89, 13, 243, 56, 67, 311, 431, 111, 141]
# for i in ls.copy():
#     if is_prime(i) == True:
#         ls.remove(i)  # 此处为一行代码
# print(len(ls))





# f0 = open('SunSign.csv','r',encoding='utf-8')
# llist= []
# for line in f0:
#     line = line.replace('\n','')
#     llist.append(line.split(','))
# f0.close()
# while True:
#     user = input()
#     if user == 'exit':
#         break
#     for lines in llist:
#         if user == lines[0]:
#             print('{0}座的日期在{1}-{2}之间'.format(chr(eval(lines[3])),lines[1],lines[2]))
#         else:
#             print('输入星座名称有误！')



# fweb = open('txt\\论语-网络版.txt','r',encoding='utf-8')
# fwed = open('txt\\论语-提取版.txt','w',encoding='utf-8')
# flag = True
# for line in fweb:
#     if '【' in line:
#         flag = False
#     if '【原文】' in line:
#         flag = True
#         continue
#     if flag == True:
#         line = line.replace('·','').replace('(','').replace(')','')
#         for word in line:
#             if word.isdigit():
#                 line = line.replace(word,'')
#         fwed.write(line)
# fweb.close()
# fwed.close()   # todo 文本删除指定内容


# s = '111001' # 请输入一个由1和0组成的二进制数字串：
# d = 0
# while s:
#    d = d*2 + eval(s[0])
#    s = s[1:]
# print("转换成十进制数是：{}".format(d))  # todo 有些绕的进制转换


# def test( b = 2, a = 4):
#     global z
#     z += a * b
#     return z
# z = 10
# print(z, test())
# print(z)

# import pra34


# # The main HTML for the whole page.
# PAGE_HTML = """
# <p>Welcome, {name}!</p>
# <p>Products:</p>
# <ul>
# {products}
# </ul>
# """
#
# # The HTML for each product displayed.
# PRODUCT_HTML = "<li>{prodname}: {price}</li>\n"
#
# def make_page(username, products):
#     product_html = ""
#     for prodname, price in products:
#         product_html += PRODUCT_HTML.format(prodname=prodname, price=format_price(price))
#     html = PAGE_HTML.format(name=username, products=product_html)
#     return html


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')
