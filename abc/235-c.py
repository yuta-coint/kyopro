import sys
input = sys.stdin.readline
n,q = map(int,input().split())
a = list(map(int,input().split()))
cnt = [0 for i in range(n+1)]
check = [[] for i in range(n+1)]
b=set(sorted(a))
d = {v:i for i, v in enumerate(b)}
for i in range(n):
    a[i] = d[a[i]]
    check[a[i]].append(i)
    cnt[a[i]]+=1
for i in range(q):
    x,k = map(int,input().split())
    if x in d:
        x = d[x]
    else:
        print(-1)
        continue
    if cnt[x]<k:
        print(-1)
    else:
        print(check[x][k-1]+1)



