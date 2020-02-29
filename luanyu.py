# f1 = open('txt\\论语-网络版.txt','r',encoding="UTF-8")
# print(f1.read())

with open('txt\\论语-网络版.txt','r',encoding="UTF-8") as f1,open('txt\\论语-提取版.txt','r+',encoding="UTF-8") as f2:
    for line in f1:
        for i in range(20):
            for j in range(20):
                k = '%d·%d' % (i,j)
                line = line.replace(k,'')
        line = line.replace('\n','')
        f2.write(line.lstrip().rstrip()+'\n')
f2 = open('txt\\论语-提取版.txt','r+',encoding="UTF-8",errors='ignore')
# f2.truncate()
print(f2.read())
# s="我是一个人(中国人)aaa[真的]bbbb{确定}"
# a = re.sub(u"\\(.*?\\)|{.*?}|\\[.*?]", "", s)
# print (a)