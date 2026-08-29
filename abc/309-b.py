N = int(input())
from copy  import deepcopy
A = [list(input()) for i in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j]=int(A[i][j])
ans = deepcopy(A)
for i in range(N-1):
    ans[i][0]=A[i+1][0]
    ans[0][i+1]=A[0][i]
    ans[i+1][N-1] = A[i][N-1]
    ans[N-1][i]=A[N-1][i+1]
for i in range(N):
    print(*ans[i],sep="")
    
    