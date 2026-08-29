import sys
input = sys.stdin.readline
from copy import copy
N,M,K,S,T,X = map(int,input().split())
S -=1
T-=1
X-=1
mod = 998244353
G = [[] for j in range(N)]
ansodd = [0 for i in range(N)]
anseven = [0 for i in range(N)]
for i in range(M):
    u,v = map(lambda x:int(x)-1,input().split())
    G[u].append(v)
    G[v].append(u)
anseven[S]=1
for _ in range(K):
    tempodd=[0 for i in range(N)]
    tempeven=[0 for i in range(N)]
    for i in range(N):
        for j in G[i]:
            if j==X:
                tempodd[j]+=anseven[i]
                tempodd[j]%=mod
                tempeven[j]+=ansodd[i]
                tempeven[j]%=mod
            else:
                tempodd[j]+=ansodd[i]
                tempodd[j]%=mod
                tempeven[j]+=anseven[i]
                tempeven[j]%=mod
    anseven = copy(tempeven)
    ansodd = copy(tempodd)
print(anseven[T])
