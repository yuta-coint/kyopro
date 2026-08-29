import sys
input = sys.stdin.readline
n,k,l = map(int,input().split())
G = [[] for i in range(n)]
R = [0 for i in range(n)]
for _ in range(k):
    p,q = map(lambda x:int(x)-1,input().split())
    G[p].append(q)
    G[q].append(p)
check = [True for i in range(n)]
S = []
cnt = 0
for i in range(n):
    if check[i]==False:
        continue
    check[i]=False
    S.append(i)
    while S!=[]:
        v = S.pop()
        R[v]=cnt
        for w in G[v]:
            if check[w]:
                R[w]=cnt
                check[w]=False
                S.append(w)
    cnt+=1
G = [[] for i in range(n)]
T = [0 for i in range(n)]
for _ in range(l):
    p,q = map(lambda x:int(x)-1,input().split())
    G[p].append(q)
    G[q].append(p)
check = [True for i in range(n)]
S = []
cnt = 0
for i in range(n):
    if check[i]==False:
        continue
    check[i]=False
    S.append(i)
    while S!=[]:
        v = S.pop()
        T[v]=cnt
        for w in G[v]:
            if check[w]:
                T[v]=cnt
                check[w]=False
                S.append(w)
    cnt+=1

ans = [0 for i in range(n)]
a = [(R[i],T[i],i) for i in range(n)]
a.sort()
cnt = 1
S = [a[0][2]]
for i in range(1,n):
    if a[i][1]==a[i-1][1] and a[i][0]==a[i-1][0]:
        cnt+=1
        S.append(a[i][2])
    else:
        for t in S:
            ans[t]=cnt
        S = [a[i][2]]
        cnt=1
for t in S:
    ans[t]=cnt
print(*ans)

