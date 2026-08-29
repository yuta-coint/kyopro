from itertools import product
import sys
input = sys.stdin.readline
N,W,P = map(int,input().split())
A = list(map(int,input().split()))
A1 = A[:N//2]
A2 = A[N//2:]
b1 = [[] for i in range(N//2+1)]
b2 = [[] for i in range(N+1//2+1)]
for bits in product([0,1],repeat=N//2):
    c = 0
    v = 0
    for a,s in zip(A1,bits):
        c+=s
        v+=a*s
    b1[c].append(v)
for bits in product([0,1],repeat=(N+1)//2):
    c = 0
    v = 0
    for a,s in zip(A2,bits):
        c+=s
        v+=a*s
    b2[c].append(v)
for b in b1:b.sort()
for b in b2:b.sort()
ans = 0
#print(b1)
#print(b2)
for i in range(N//2+1):
    #A1からi個A2からW-i個
    if W-i<0 or W-i>=N+1//2+1:
        continue
    cnt = len(b2[W-i])-1
    for j in b1[i]:
        while cnt>=0:
            if b2[W-i][cnt]+j<=P:
                break
            cnt-=1
        ans+=cnt+1
print(ans)