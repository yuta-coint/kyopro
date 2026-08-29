import sys
input = sys.stdin.readline
def main():
    mod = 998244353
    N,M,K = map(int,input().split())
    G = [[] for j in range(N)]
    for _ in range(M):
        u,v = map(lambda x:int(x)-1,input().split())
        G[u].append(v)
        G[v].append(u)
    o=0
    e=0
    ds = 0
    for i in range(N):
        ds+=len(G[i])
        if len(G[i])&1:
            o+=1
        else:
            e+=1
    #M:evenで次数の総和がevenの時を考える
    ans =0
    ##########combination求めるときの前計算
    powers = [1]
    p=1
    for i in range(1,10**6+1):
        p*=i
        p%=mod
        powers.append(p)
    mother = powers[10**6]
    mothers = []
    mother = pow(mother,mod-2,mod)
    for i in reversed(range(1,10**6+1)):
        mothers.append(mother)
        mother*=i
        mother%=mod
    mothers.reverse()
    mothers = [1]+mothers
    ##############################
    for i in range(0,K+1,2):
        if o-i >=0 and e-K+i>=0:
            ans += powers[o]*powers[e]%mod*mothers[o-i]%mod*mothers[i]%mod*mothers[K-i]%mod*mothers[e-K+i]%mod
            ans%=mod
    #print(powers)
    print(ans)
main()