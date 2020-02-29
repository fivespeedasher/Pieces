line3 = ''
import re
with open('txt\\论语-提取版.txt','r+',encoding="UTF-8") as f2,open('txt\\论语-原文.txt','w',encoding="UTF-8") as f3:
    for line in f2.readlines() :

        line3 = line3 + line
        line3 = re.sub(u'\(\d\)','',line3)
        # if line == '】':
        #     del line3[-4, -1]
        #     continue


    f3.write(line3)
# f3=open('txt\\论语-原文.txt','r+',encoding="UTF-8")
# f3.truncate()
# f3.close()