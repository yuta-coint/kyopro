
def first_one(M):
    cnt = M
    for i in range(2,N+1):
        if cnt%i == 0:
            return i-1
        else:
            cnt -= cnt//i
    return N
N,K = map(int,input().split())
FO = []
counter = 0
while counter <= K and counter <=10**4:
    A = first_one(-counter+K)
    FO.append(A)
    counter+=1
counter-=1
FO.reverse()
t = 1
while t <=10**4:
    A = first_one(t+K)
    FO.append(A)
    t+=1
t-=1
L = len(FO)
from sortedcontainers import SortedSet
ans = [[-1 for j in range(L)] for i in range(N)]
ans[0] = [0 for j in range(L)]
mae = [(0,i) for i in range(L)]
for i in range(1,N):
    for j in range(L):
        ans[i][j] = ans[i-1][j]
    chk = [SortedSet() for i in range(i+1)]
    for s,j in mae:
        chk[s].add(j)
    up = set()
    for s,j in mae:
        if FO[j]>i:
            ans[i][j] = 0
            continue
        if FO[j]==i or (j in up):
            ans[i][j] += 1
            c = chk[s+1].bisect_left(j)
            if c!=0:
                up.add(chk[s+1][c-1])
            if c!=len(chk[s+1]):
                up.add(chk[s+1][c])
    mae = [(ans[i][j],j) for j in range(L)]
    mae.sort()
out = []
usiro = []
for i in range(N-1):
    if ans[i][counter]==ans[i+1][counter]:
        out.append("D")
        usiro.append("R")
    else:
        out.append("R")
        usiro.append("D")
usiro.reverse()
out = out+usiro
print(*out,sep="")
