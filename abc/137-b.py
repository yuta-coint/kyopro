N = int(input())
a = list(map(int,input().split()))
sa = [0]
for i in range(N):
    if a[i]==0:
        sa.append(sa[-1]-1)
    else:
        sa.append(sa[-1]+1)
ma = -float('inf')
mi = float('inf')
m = 0
M = 0
for i in range(N+1):
    mi = min(mi,sa[i])
    ma = max(ma,sa[i])
    m = max(m,sa[i]-mi)
    M  =max(M,ma-sa[i])
print(M+m+1)

