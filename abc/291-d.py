mod = 998244353
N = int(input())
AB = [tuple(map(int,input().split())) for i in range(N)]
dpa = [0 for i in range(N)]
dpb = [0 for i in range(N)]
dpa[0]=1
dpb[0]=1
for i in range(1,N):
    if AB[i][0]!=AB[i-1][0]:
        dpa[i]+=dpa[i-1]
    if AB[i][0]!=AB[i-1][1]:
        dpa[i]+=dpb[i-1]
    if AB[i][1]!=AB[i-1][0]:
        dpb[i]+=dpa[i-1]
    if AB[i][1]!=AB[i-1][1]:
        dpb[i]+=dpb[i-1]
    dpa[i]%=mod
    dpb[i]%=mod
print((dpa[-1]+dpb[-1])%mod)