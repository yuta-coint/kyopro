ab = {}
cd = {}
n,v = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if a[i]+b[j] in ab:
            ab[a[i]+b[j]]+=1
        else:
            ab[a[i]+b[j]]=1
        if c[i]+d[j] in cd:
            cd[c[i]+d[j]]+=1
        else:
            cd[c[i]+d[j]]=1
ans = 0
for i in ab:
    if v-i in cd:
        ans+=ab[i]*cd[v-i]
print(ans)
