lowern = eval(input('input a start number'))
uppern = eval(input('input a last number'))
def susu(n,m):
    s=[]
    for i in range(n,m+1):
        if i>1:
            for k in range(2,i):
                if i%k==0:
                    break
                elif k == i-1:
                    s.append(i)
    print(s)
susu(lowern,uppern)

