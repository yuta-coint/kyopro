N,K = map(int,input().split())
P = list(map(lambda x:int(x)-1,input().split()))
rP = [-1 for i in range(N)]
for i in range(N):
    rP[P[i]] = i
rans = [-1 for i in range(N)]
ans = [-1 for i in range(N)]
for i in range(N):
    if ans[i]!=-1:
        continue
    cyc = [i]
    t = P[i]
    while t!=i:
        cyc.append(t)
        t = P[i]
    loop = len(cyc)
    t = pow(2,K,loop)
    for j in range(loop):
        ans[cyc[i]] = cyc[(i+t)%loop]
for i in range(N):
    ans[i]+=1
print(*ans)
    
