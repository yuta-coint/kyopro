N,M = map(int,input().split())
check = [[0 for i in range(N)] for i in range(M)]
for i in range(M):
    C = int(input())
    a = list(map(int,input().split()))
    for j in range(C):
        check[i][a[j]-1]=1
from itertools import product
ans = 0
for bits in product(range(2),repeat=M):
    temp = [0 for i in range(N)]
    for i in range(M):
        if bits[i]==1:
            for j in range(N):
                temp[j]|=check[i][j]
    if sum(temp)==N:
        ans+=1
print(ans)
