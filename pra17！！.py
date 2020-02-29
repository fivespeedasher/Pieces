# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
import collections
import string
text=open('D:\I\'M\\usedbypython\\1.txt').read()
row=len(open('D:\I\'M\\usedbypython\\1.txt').readlines())
letter=0
digit=0
punc=0
space=0
zh=0
for i in range (len(text)):
    c=text[i]
    if c in string.ascii_letters:
        letter+=1
    elif c.isdigit():
        digit+=1
    elif c.isspace():
        space+=1
    elif  c.isalpha():
        zh+=1
    else:
        punc+=1
print('en=',letter,'\ndigit=',digit,'\nspace=',space,'\nzh=',zh,'\npunctuation',punc,'\nrow=',row)