import jieba

# s = '“工业互联网”实施的方式是通过通信、控制和计算技术的交叉应用，建造一个信息物理系统，促进物理系统和数字系统的融合。'
s = input("请输入一个中文字符串，包含逗号和句号：")
s = s.replace('，','').replace('。','').replace('、','').replace('“','').replace('”','')
k=jieba.lcut(s)
d1 = {}
maxc = 0
wo = ''
for i in k:
   print(i, end= "/ ")
   d1[i] = d1.get(i,0) + 1
print("\n中文词语数是：{}".format(len(k)))

for key in d1:
    if maxc < d1[key]:
        wo = key
        maxc = d1[key]
    elif maxc == d1[key]:
        wo += ' ' + key
    print("{}: {}".format(key,d1[key]))
    '''
    筛选最多的元组
    '''

print("出现最多的词是（{}）：{} 次".format(wo, maxc))
'''排序
    items():以列表返回遍历的（键：值）元组'''
d2 = sorted(d1.items(),key=lambda x:x[1],reverse=True)
print(d2)