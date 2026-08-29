#RMQ
N,Q = map(int,input().split())
c = 1
n = 1
while c<N:
    c*=2
    n+=1
INF = 2**31-1
SEG = [INF for i in range(2**n)]#n段のセグ木
def update(i,a):
    i += 2**(n-1)
    SEG[i]=a
    while i>1:
        i //= 2
        SEG[i] = min(SEG[2*i],SEG[2*i+1])
def find(s,t):
    k = INF
    s += 2**(n-1)
    t += 2**(n-1)
    while s<=t:
        if s%2==1:
            k = min(k,SEG[s])
            s//=2
            s+=1
        else:
            s//=2
        if t%2==0:
            k = min(k,SEG[t])
            t//=2
            t-=1
        else:
            t//=2
    return(k)

#香辛料igを消費することで作れる最大の価値,マイナスで管理
update(0,0)
for i in range(Q):
    l,r,v = map(int,input().split())
    for j in reversed(range(l,N+1)):
        r = min(j,r)
        f = find(j-r,j-l)
        if f!=INF and f-v<find(j,j):
            update(j,f-v)
if find(N,N)==INF:
    print(-1)
else:
    print(-find(N,N))
