N= int(input())
P = list(map(int,input().split()))
r = 1
ans = [-1 for i in range(N)]
while min(ans)==-1:
    x = max(P)
    k = P.count(x)
    for i in range(N):
        if P[i]==x:
            ans[i]=r
            P[i]=-1
    r+=k
print(*ans)