import sys
input = sys.stdin.readline
N = int(input())
boxes = []
for i in range(N):
    hwd = list(map(int,input().split()))
    hwd.sort()
    boxes.append([hwd[0],-hwd[1],-hwd[2]])
boxes.sort()
#とりあえずwを座標圧縮
a = [boxes[i][1] for i in range(N)]
b = sorted(set(a))
d = {v:i for i, v in enumerate(b)}
for i in range(N):
    boxes[i][1]=d[boxes[i][1]]
#RMQ
c = 1
n = 1
while c<N+2:
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
    return k
#各幅超過の中で奥行きが一番小さいものを探る
cnt = 0
for i in range(N):
    w,d =boxes[i][1],-boxes[i][2]
    if find(w+1,N+1) < d:
        print("Yes")
        exit()
    if d<find(w,w):
    	update(w,d)
print("No")