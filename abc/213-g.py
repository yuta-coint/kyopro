N,M = map(int,input().split())
G = [[False for i in range(N)] for j in range(N)]
mod = 998244353
for i in range(M):
    a,b = map(int,input().split())
    G[a-1][b-1] = 1
    G[b-1][a-1] = 1
ans = [0 for i in range(1<<N)]
all_ans = [0 for i in range(1<<N)]
strong = [False for i in range(1<<N)]
pr = [0 for i in range(N)]
for bits in range(1<<N):
    #bitsの中に何個辺があるか
    ed = 0
    free=0
    for i in range(N-1):
        for j in range(i+1,N):
            if (bits>>i)&1 and (bits>>j)&1:
                ed += G[i][j]
            elif (not((bits>>i)&1)) and (not((bits>>j)&1)):
                free += G[i][j]
    all_ans[bits] = pow(2,ed,mod)
    ans[bits] = all_ans[bits]
    subset = (bits-1)&bits
    top = -bits & bits
    while subset:
        if subset&top>0:
            ans[bits]-=all_ans[bits-subset]*ans[subset]%mod
            ans[bits]%=mod
        subset = (subset-1)&bits
    if bits&1:
        for i in range(N):
            if (bits>>i)&1:
                pr[i]+=ans[bits]*pow(2,free,mod)
                pr[i]%=mod
#print(ans)
#print(pr)
for i in range(1,N):
    print(pr[i])