#何個辺を採用できるかを調べればよい。
#連結成分が3個になることはない
from itertools import permutations
N,M = map(int,input().split())
C = 100
edges = set()
for i in range(M):
    a,b = map(int,input().split())
    edges.add((a-1)*C+(b-1))
    edges.add((b-1)*C+(a-1))
cut = []
for i in range(N+1):
    if i>=3 and (N-i)>=3:
        cut.append(i)
tyofuku = 0
for p in permutations(range(1,N)):
    cnt = 0
    temp = 0
    for k in p:
        if k*100 + temp in edges:
            cnt += 1
        temp = k
    if temp in edges:
        cnt += 1
    if cnt>tyofuku:
        tyofuku = cnt
    for c in cut:
        cnt = 0
        temp = 0
        for i in range(c-1):
            if p[i]*100 + temp in edges:
                cnt+=1
            temp = p[i]
        if temp in edges:
            cnt += 1
        start = p[c-1]
        temp = p[c-1]
        for i in range(c,N-1):
            if p[i]*100 + temp in edges:
                cnt+=1
            temp = p[i]
        if start*100 + temp in edges:
            cnt += 1
        if cnt > tyofuku:
            tyofuku = cnt
print(M+N-2*tyofuku)