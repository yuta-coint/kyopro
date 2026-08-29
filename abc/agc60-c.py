mod = 998244353
N,A,B=map(int,input().split())
from itertools import combinations
ans = 0
all = 0
for p in combinations(range(6),3):
    two = 0
    for i in range(6):
        if i in p:
            continue
        two = i
        break
    if p[1]<two:
        ans+=1
    if p[2]<two:
        ans+=1
    all += 2
print(ans,all)