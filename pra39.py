ls = [1,10,15,20,25,30,35,40,45,50]
new = eval(input('enter a number'))
# ls.insert(1,new)
# ls.sort(reverse=False)
# print(ls)

ls.append(0)
if new > ls[-2]:
    ls[-1] = new
else:
    for i in range(len(ls)):
        if ls[i] > new:
            temp1 = ls[i]
            ls[i] = new
            for k in range (i+1,len(ls)):
                temp2 = ls[k]
                ls[k] = temp1
                temp1 =temp2
            break
                # try:
                #     temp1 = ls[k+1]
                # except:
                #     break

print(ls)