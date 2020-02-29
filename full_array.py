n = int(input("scale:"))
def fullit(matrix):
    m = 0
    i = 0
    j = n//2
    res = 1
    matrix[i][j] = res
    while(m<n*n-1):
        m += 1
        res +=1
        if(matrix[(i-1)%n][(j-1)%n]==0):
            matrix[(i-1)%n][(j-1)%n] = res
            i = (i-1)%n
            j = (j-1)%n
        else:
            matrix[(i+1)%n][j] = res
            i = (i+1)%n
    for k in matrix:
        print(k)
matrix = [([0]*n)for i in range (n)]
fullit(matrix)

