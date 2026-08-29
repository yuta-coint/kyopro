def pr(M):
    for l in M:
        print(*l)
#i列目をs倍してj列目に足す。
def column(i,j,s):
    for k in range(d):
        mat[k][j]+=mat[k][i]*s
r=4
q=3
d = r*q+1
mat = [[0 for j in range(d)] for i in range(d)]
poly = [0,3,3,1]
for i in range(d):
    for j in range(d):
        if 0<=i-j<=3:
            mat[i][j] = poly[i]
#下の方から掃き出しを行う。
for x in reversed(range(q*(r-1))):
    for y in range(q*(r-1),q*r):
        column(x,y,-mat[x+q][y])
    pr(mat)