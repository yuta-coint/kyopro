#RMQ
N = int(input())
c = 1
n = 1
while c<N:
    c*=2
    n+=1
INF = 0
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
h=list(map(int,input().split()))
h = [(h[i],i) for i in range(N)]
h.sort()
a=list(map(int,input().split()))
for i in range(N):
    update(h[i][1],find(0,h[i][1])-a[h[i][1]])
    #print(h[i][1],find(0,h[i][1])-a[h[i][1]])
print(-find(0,N-1))