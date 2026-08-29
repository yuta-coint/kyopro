N,M=map(int,input().split())
G = [[] for i in range(N)]
for i in range(M):
    l,d,k,c,A,B = map(int,input().split())
    G[B-1].append((A-1,l,d,k,c))
from heapq import heapify,heappop,heappush
q = [(-10**24,N-1)]
last_train = [-10**24 for i in range(N)]
heapify(q)
seen = [False] * N
while q!=[]:
    #終電が一番遅い、すなわち値が一番小さい
    lt,sta = heappop(q)
    if seen[sta]==True:
        continue
    seen[sta] = True
    lt = -lt
    for A,l,d,k,c in G[sta]:
        #A駅から時刻ltに間に合わせるのに一番遅い時刻を計算する
        if l+c>lt:
            continue
        if l+c+(k-1)*d<=lt:
            if last_train[A]<l+(k-1)*d:
                last_train[A]=l+(k-1)*d
                heappush(q,(-(l+(k-1)*d),A))
        else:
            num = (lt-l-c)//d
            if last_train[A] < l+num*d:
                last_train[A] = l+num*d
                heappush(q,(-(l+num*d),A))
for i in range(N-1):
    if last_train[i]==-10**24:
        print("Unreachable")
    else:
        print(last_train[i])