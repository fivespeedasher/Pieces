#   两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和
# x,z比，请编程序找出三队赛手的名单。

# jteam=['a','b','c']
# yteam=['x','y','z']
# list1=[]
# for i in range(3):
#     # for jteam[i] in list1:  TODO 为什么这步不执行？
#         if i==3:
#             list1.append(yteam[1])
#             list1.append('\n')
#         elif i==1:
#             list1.append(yteam[2])
#             list1.append('\n')
#         else:
#             list1.append(yteam[0])
# print(list1)


for i in range(ord('x'),ord('z')+1):
    for j in range(ord('x'),ord('z')+1):
        if i!=j :
            for k in range(ord('x'), ord('z')+1):
                if i!=k and j!=k:
                    if i!=ord('x') and k!=ord('x') and k!=ord('z') :
                        print("match is a-->%s\t\tb-->%s\t\tc-->%s"%(chr(i),chr(j),chr(k)))