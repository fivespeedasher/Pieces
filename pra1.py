#1234能组成多少个互不相同 无重复数字的三位数
for s in range(1,5):
    for t in range(1,5):
        for h in range(1,5):
            if s!=t!=h:
                print(s,t,h)

