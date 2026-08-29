N = int(input())
d = {}
for i in range(N):
    a,c = map(int,input().split())
    if c in d:
        d[c] = min(a,d[c])
    else:
        d[c] = a
ans = 0
for t in d:
    if d[t]>ans:
        ans = d[t]
print(ans)