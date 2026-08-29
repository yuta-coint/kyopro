N,M,L = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
big = 10**9
bad_pair = set()
for i in range(L):
    c,d = map(lambda x:int(x)-1,input().split())
    bad_pair.add(c*big+d)
a = [(a[i],i) for i in range(N)]
b = [(b[i],i) for i in range(M)]
a.sort(reverse=True)
b.sort(reverse=True)
#既に確認し終えた副菜
from heapq import heapify,heappop,heappush
eaten = set([0])
cand = [(-a[0][0]-b[0][0],0)]
heapify(cand)
while True:
    chk = heappop(cand)
    syu = chk[1]//big
    fuku = chk[1]%big
    if not (a[syu][1]*big+b[fuku][1] in bad_pair):
        print(-chk[0])
        break
    if syu<N:
        if not ((syu+1)*big+fuku in eaten):
            heappush(cand,(-a[syu+1][0]-b[fuku][0],(syu+1)*big+fuku))
            eaten.add((syu+1)*big+fuku)
    if fuku<M:
        if not syu*big+fuku+1 in eaten:
            heappush(cand,(-a[syu][0]-b[fuku+1][0],syu*big+fuku+1))
            eaten.add(syu*big+fuku+1)