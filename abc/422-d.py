N,K = map(int,input().split())
ans = [-1,K]
for i in range(2,1<<(N+1)):
    if i&1:
        ans.append((ans[i//2]+1)//2)
    else:
        ans.append(ans[i//2]//2)
X = 0
for i in range(1,N+1):
    ma = -1
    mi = 10**24
    for j in range(1 << i,1 << (i+1)):
        if ans[j] > ma:
            ma = ans[j]
        if ans[j] < mi:
            mi = ans[j]
    if ma - mi > X:
        X = ma - mi
print(X)
print(*ans[1 << N:1 << (N+1)])
            