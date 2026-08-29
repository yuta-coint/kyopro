mod = 10**9+7
sana = 372803
N,Q = map(int,input().split())
#前半を普通の文、後半を逆向きにした文にする
#RSQ
n=2*N
#n:数列の長さ
BIT = [0 for i in range(n+1)]
def add(i,x):
    while i<=n:
        BIT[i]+=x
        i += (i&-i)
#xまでの和をとる
def getSum(x):
    i = x
    gs = 0
    while i>0:
        gs+=BIT[i]
        i -= (i&-i)
    return gs
S = input()
So = []
H = []
T = []
tun = 1
tuntun = []
for i in range(N):
    tuntun.append(tun)
    k = ord(S[i])-ord("a")
    So.append(k)
    add(i+1,k*tun%mod)
    k = ord(S[N-i-1])-ord("a")
    add(N+i+1,k*tun%mod)
    tun*=sana
    tun%=mod
nutnut = []
nut = pow(tun,mod-2,mod)
for i in range(N):
    nut*=sana
    nut%=mod
    nutnut.append(nut)
nutnut.reverse()
for i in range(Q):
    query = list(input().split())
    if int(query[0])==1:
        x = int(query[1])
        #どれくらい増やすか
        c = ord(query[2])-ord("a")-So[x-1]
        So[x-1]+=c
        add(x,c*tuntun[x-1]%mod)
        add(2*N-x+1,c*tuntun[N-x]%mod)
    else:
        L,R=int(query[1]),int(query[2])
        temp1 = (getSum(R)-getSum(L-1))%mod
        temp1*=nutnut[L-1]
        temp1%=mod
        temp2 = (getSum(2*N+1-L)-getSum(2*N-R))%mod
        temp2*=nutnut[N-R]
        temp2%=mod
        if temp1==temp2:
            print("Yes")
        else:
            print("No")