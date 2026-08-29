N = int(input())
ori = set()
ma = -1
ans = -1
for i in range(1,N+1):
    s,t = input().split()
    t = int(t)
    if s in ori:
        continue
    ori.add(s)
    if t>ma:
        ans=i
        ma=t
print(ans)

