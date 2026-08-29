mod = 998244353
N,H = map(int,input().split())
X = list(map(int,input().split()))
pole = [(X[i],i) for i in range(N)]
pole.sort()
group = [[pole[0][1]]]
g = 0
belong = [-1 for i in range(N)]
belong[pole[0][1]]=0
for i in range(1,N):
    if pole[i-1][0]+H<pole[i][0]:
        group.append([])
        g+=1
    group[g].append(pole[i][1])
    belong[pole[i][1]]=g
grpsize = [len(group[i]) for i in range(g+1)]
#左隣と右隣はすでに倒れているか。ただし、いなければ倒れている扱い。
killed = [0 for i in range(N)]
for t in range(g+1):
    for s in range(grpsize[t]):
        if s==0:
            killed[group[t][s]]+=1
        else:
            if group[t][s]>group[t][s-1]:
                killed[group[t][s]]+=1
        if s==grpsize[t]-1:
            killed[group[t][s]]+=1
        else:
            if group[t][s]>group[t][s+1]:
                killed[group[t][s]]+=1
chk = [0 for i in range(g+1)]
cnt = [0 for i in range(g+1)]
pow2 = [1]
for i in range(N):
    pow2.append(pow2[-1]*2%mod)
zero = g+1
#0を除いた積
ans = 1
out = []
#print(cnt)
for i in range(N):
    #print(cnt)
    #print(grpsize)
    old = chk[belong[i]]
    cnt[belong[i]]+=1
    chk[belong[i]]+=(pow2[grpsize[belong[i]]-cnt[belong[i]]]*killed[i])%mod
    chk[belong[i]]%=mod
    if old == 0 and chk[belong[i]]>0:
        zero-=1
        ans*=chk[belong[i]]
        ans%=mod
    elif old>0 and chk[belong[i]]==0:
        ans*=pow(old,-1,mod)
        ans%=mod
        zero+=1
    elif old>0 and chk[belong[i]]>0:
        ans*=chk[belong[i]]
        ans%=mod
        ans*=pow(old,-1,mod)
        ans%=mod
    if zero>0:
        out.append(0)
        continue
    out.append(ans)
for i in reversed(range(1,N)):
    out[i]-=out[i-1]
    out[i]%=mod
print(*out)