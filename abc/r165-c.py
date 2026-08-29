import sys
input = sys.stdin.readline
N,M = map(int,input().split())
G = [set() for i in range(N)]
for i in range(M):
    a,b,w = map(int,input().split())
    G[a-1].add((b-1,w))
    G[b-1].add((a-1,w))
ok = 0
ng = 10**16
#各頂点のワースト2を足し合わせた最小値を考える
for i in range(N):
    first = 10**16
    second = 10**16
    for v,w in G[i]:
        if w<first:
            second = first
            first = w
        elif w<second:
            second = w
    if first+second+1<ng:
        ng = first+second+1
from collections import deque
while ok+1<ng:
    X = (ok+ng)//2
    color = [-1 for i in range(N)]
    #X未満のやつを無視して二色に塗り分けられるかを調べればいい
    flag = 0
    next = deque()
    for i in range(N):
        if color[i]!=-1:
            continue
        color[i]=0
        next.append(i)
        while next:
            k = next.pop()
            for v,w in G[k]:
                if w>=X:
                    continue
                if color[v]==color[k]:
                    flag=1
                    break
                if color[v]==-1:
                    next.append(v)
                    color[v]=1-color[k]
            if flag==1:
                break
        if flag==1:
            break
    if flag==0:
        ok = X
    else:
        ng = X
print(ok)