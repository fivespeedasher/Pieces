#题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
for i in range(1,85):
    j=168/i
    n=(i-j)/2
    m=(i+j)/2
    if m*m-n*n==168 and (n*n-100)%1==0 and i>j :
        print(n*n-100) 