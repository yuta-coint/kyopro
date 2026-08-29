N,M,K = map(int,input().split())
mod = 998244353
inv=[pow(i,mod-2,mod) for i in range(3001)]
G = [[] for i in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
dim = [inv[len(G[i])] for i in range(N)]
C = list(map(int,input().split()))
growth = [0 for i in range(N)]
attack = [0 for i in range(N)]
prob = [0 for i in range(N)]
prob[0]=1
growth[0]=1
ans = 0
for _ in range(K):
    #もらえるお金の増え幅の期待値×確率
    growth_new = []
    #もらえるお金の期待値×確率
    attack_new = []
    #そこにいる確率
    prob_new = []
    for i in range(N):
        g,a,p = 0,0,0
        for node in G[i]:
            g+=dim[node]*growth[node]%mod
            g%=mod
            a+=dim[node]*attack[node]%mod
            a%=mod
            p+=dim[node]*prob[node]%mod
            p%=mod
        #print(g,a,p,s)
        if C[i]==1:
            ans+=a
            ans%=mod
        else:
            a+=g
            a%=mod
            g+=2*p%mod
            g%=mod
        growth_new.append(g)
        attack_new.append(a)
        prob_new.append(p)
    growth = growth_new
    attack = attack_new
    prob = prob_new
print(ans)