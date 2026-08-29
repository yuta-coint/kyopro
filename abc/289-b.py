N,M = map(int,input().split())
a = list(map(int,input().split()))
check = [0 for i in range(N)]
for i in range(M):
    check[a[i]-1]=1
ans = []
stk = []
for i in range(N):
    stk.append(i+1)
    if check[i]==0:
        stk.reverse()
        ans+=stk
        stk = []
print(*ans)