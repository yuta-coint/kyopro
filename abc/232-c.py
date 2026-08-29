n,m = map(int,input().split())
import itertools
arr = [i for i in range(n)]
ptn = list(itertools.permutations(arr))
path=[]
taka = [set() for i in range(n)]
aoki = [set() for i in range(n)]
for i in range(m):
    a,b = map(lambda x:int(x)-1,input().split())
    taka[a].add(b)
    taka[b].add(a)
for i in range(m):
    c,d = map(lambda x:int(x)-1,input().split())
    aoki[d].add(c)
    aoki[c].add(d)
for p in ptn:
    taka1 = [set() for i in range(n)]
    for i in range(n):
        for j in taka[i]:
            taka1[p[i]].add(p[j])
    if taka1==aoki:
        print("Yes")
        break
else:
    print("No")