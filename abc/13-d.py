n,m,d =map(int,input().split())
a = list(map(int,input().split()))
p = [i for i in range(n)]
for i in range(m):
    p[a[i]-1],p[a[i]] = p[a[i]],p[a[i]-1]
#ans.append(p)
ans = [i for i in range(n)]
for i in reversed(range(len(bin(d))-2)):
    ans = [ans[ans[j]] for j in range(n)]
    if d>>i & 1 == 1:
        ans = [ans[p[j]] for j in range(n)]
a = [0 for i in range(n)]
for i in range(n):
    a[ans[i]] = i
for i in range(n):
    ans.append(a[i]+1)