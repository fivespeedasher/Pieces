pt=open('C:\\Users\\asshole\Anaconda3\Lib\\this.py')
pt.read()
for p in pt:
    if 'a'<= p<='z':
        print(chr(ord('a')+(ord(p)-ord('a')+3)%26),end='')
    elif 'A'<= p<='Z':
        print(chr(ord('a')+(ord(p)-ord('a')+3)%26),end='')
    else:
        print(p,end='')