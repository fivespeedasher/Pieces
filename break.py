

while True:
    i=input('Enter something')
    if i=='stop':
        break
    if len(i)<3:
        continue

    print('Length is',len(i))

# 怎么让输入的字符在下一行