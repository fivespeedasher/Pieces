# f1 = open('trytttxt.txt','w')
# f1.write('Hello at the first row')
# f1.close()
# with open('txt\\food.txt','r+') as f2 :
#     for lines in f2.readlines():

with open('txt\\food.txt','r') as f2, open('txt\\food2.txt','r+') as linef:
# f2.write('11111111\n1111111111')
# for f2 in open('txt\\food.txt'):
#     print(f2)
# print(f2.readlines())
    for line in f2:
        if '\n' in line:
            line=line.replace('\n','空行')
        linef.write(line)

    print(linef.readlines())
f2=open('txt\\food.txt','r')
print(f2.read())  # TODO 这里输出的元素为0？
