import bisect
N,Q = map(int,input().split())
c = 1
n = 1
while c<N:
    c*=2
    n+=1
INF = 2**31-1
SEG = [INF for i in range(2**n)]#n段のセグ木
label = [i-2**(n-1) for i in range(2**n)]
def update(i,a):
    i += 2**(n-1)
    SEG[i]=a
    while i>1:
        i //= 2
        SEG[i] = min(SEG[2*i],SEG[2*i+1])
        if SEG[2*i]<SEG[2*i+1]:
            label[i] = SEG[2*i]
        else:
            label[i] = SEG[2*i+1]
def find(s,t):
    k = INF
    L=0
    s += 2**(n-1)
    t += 2**(n-1)
    while s<=t:
        if s%2==1:
            k = min(k,SEG[s])
            if k>SEG[s]:
                L = label[s]
            s//=2
            s+=1
        else:
            s//=2
        if t%2==0:
            k = min(k,SEG[t])
            if k>SEG[t]:
                L = label[t]
            t//=2
            t-=1
        else:
            t//=2
    return k,L
H = list(map(int,input().split()))
for i in range(N):
    update(i,-H[i])
#l以上r未満の中で、一番でかいのがどこにあるのかを調べる。
qr = [tuple(map(int,input().split())) for i in range(Q)]
chk = [[] for i in range(N)]
cnt = 0
for l,r in qr:
    k,L = find(l,r-1)
    chk[r].append((cnt,k))
    cnt+=1
    #Lから始まる最長単調列を答える。
SQ = [10**24]
ans = [0 for i in range(Q)]
ls = 1
for i in reversed(range(N)):
    while H[i]>SQ[-1]:
        SQ.pop()
        ls-=1
    SQ.append(H[i])
    ls+=1
    for cnt,k in chk[N]:
        ans[cnt] = bisect.bisect_right(k)-1
for i in range(Q):
    print(ans[i])