pascal_size=  1000
mod = 998244353
pascal = [[0 for i in range(pascal_size)] for j in range(pascal_size)]
for i in range(pascal_size):
    for j in range(pascal_size):
        if i ==0 and j==0:
            pascal[0][0]=1
        if i>0:
            pascal[i][j]+=pascal[i-1][j]
        if j>0:
            pascal[i][j]+=pascal[i][j-1]
        pascal[i][j]%=mod