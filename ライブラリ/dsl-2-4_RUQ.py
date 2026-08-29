#セグ木は某サイトとは異なり1からスタートしている
#https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_D
#RUQ
N,q = map(int,input().split())
c = 1
n = 1
while c<N:
    c*=2
    n+=1
INF = 2**31-1
SEG = [(INF,-1) for i in range(2**n)]#n段のセグ木
timer = 0
def find(i):
    i += 2**(n-1)
    k = SEG[i]
    while i>1:
        i //= 2
        if k[1]<SEG[i][1]:
            k=SEG[i]
    print(k[0])
def update(s,t,x):
    global timer
    k = INF
    s += 2**(n-1)
    t += 2**(n-1)
    while s<=t:
        if s%2==1:
            SEG[s] = (x,timer)
            s//=2
            s+=1
        else:
            s//=2
        if t%2==0:
            SEG[t] = (x,timer)
            t//=2
            t-=1
        else:
            t//=2
    timer+=1
for i in range(q):
    query = tuple(map(int,input().split()))
    if query[0]==0:
        update(query[1],query[2],query[3])
    else:
        find(query[1])
