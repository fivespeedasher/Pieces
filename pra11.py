# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 2，2，4，6，10，18，...(前一项-2)*2+2
a=int(input('How many months has it passed?'))
f1=1
f2=1
for i in range(2,a):
    f1+=f2
    f2=f1-f2
print(f1*2)