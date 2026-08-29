n = input()
mod = 998244353
m = int(input())
c= list(map(int,input().split()))
normal = [0 for i in range(1<<10)]
s = [0 for i in range(1<<10)]
edge = 0
edges = 0
for i in range(len(n)):
    d = int(n[i])
    temp = [0 for i in range(1<<10)]
    temp[0]=1
    temps = [0 for i in range(1<<10)]
    for k in range(10):
        temp[1<<k]+=normal[0]
        temp[1<<k]%=mod
        temps[1<<k]+=(s[0]*10+k*normal[0])%mod
        temps[1<<k]%=mod
    for j in reversed(range(2,1<<10)):
        #追加する次の桁
        for k in range(10):
            temp[j|1<<k]+=normal[j]
            temp[j|1<<k]%=mod
            temps[j|1<<k]+=(s[j]*10+k*normal[j])%mod
            temps[j|1<<k]%=mod
    for k in range(d):
        temp[edge|1<<k]+=1
        temps[edge|1<<k]+=edges*10+k
        temps[edge|1<<k]%=mod
    edge|=1<<d
    edges = (edges*10+d)%mod
    normal=temp
    s = temps
    #print(normal[2],normal[3],normal[7],normal[11],normal[19])
normal[edge]+=1
s[edge]+=edges
ans = 0
for i in range(1,1<<10):
    if i==1:
        continue
    for j in c:
        if not i&1<<j:
            break
    else:
        ans+=s[i]
        ans%=mod
print(ans)
