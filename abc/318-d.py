N = int(input())
ans = [-float("inf") for i in range(1<<N)]
G = [[0 for i in range(N)] for i in range(N)]
for i in range(N-1):
    a = list(map(int,input().split()))
    for j in range(N-i-1):
        G[i][j+i+1] = a[j]
        G[j+i+1][i] = a[j]
ans[0]=0
for bits in range(1<<N):
    for i in range(N):
        if not ((bits>>i)&1):
            continue
        for j in range(N):
            if i==j:
                continue
            if (bits>>j)&1:
                temp = ans[bits-(1<<i)-(1<<j)]+G[i][j]
                if temp>ans[bits]:
                    ans[bits]=temp
print(max(ans))