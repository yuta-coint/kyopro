import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())
D = list(map(int,input().split()))
tree = [i for i in range(N)]
def find(i):
    if tree[i] == i:
        return i
    else:
        tree[i]= find(tree[i])
        return find(tree[i])
def union(a,b):
    if tree[a] > tree[b]:
        a,b = b,a
    tree[find(b)] = find(a)
live = True
#輪っかができたら終わり
for i in range(M):
    p,q = map(lambda x:int(x)-1,input().split())
    union(p,q)
    D[p]-=1
    D[q]-=1
    if D[p]<0 or D[q]<0:
        live = False
#各グループの残っている頂点をまとめた
U = [[] for i in range(N)]
for i in range(N):
    for j in range(D[i]):
        U[find(i)].append(i)
#残っている孤立した頂点
#print(live)
D1 = []
#くっつけるべきグループ
D2 = []
for i in range(N):
    if not U[i]:
        continue
    if len(U[i])==1:
        D1.append(U[i][0])
    else:
        D2.append(i)
ans = []
for i in range(len(D2)-1):
    if U[D2[i]] and U[D2[i+1]]:
        ans.append((U[D2[i]].pop(),U[D2[i+1]].pop()))
    else:
        live = False
        break
rem = []
for i in D2:
    for j in U[i]:
        rem.append(j) 
for i in rem:
    if D1:
        ans.append((i,D1.pop()))
    else:
        live = False
        break
while len(D1)>1:
    ans.append((D1.pop(),D1.pop()))
#ほんとに木になっているのか
for i in ans:
    union(i[0],i[1])
for i in range(N):
    if find(i)!=find(0):
        live = False
if len(ans)!=N-M-1:
    live = False
if live:
    for i in ans:
        print(i[0]+1,i[1]+1)
else:
    print(-1)