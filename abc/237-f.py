mod = 998244353
N,M = map(int,input().split())
from copy import copy
#p,q,rがそれぞれ1,2,3の長さの部分列になるような場合の数
LIS1 = [1 for i in range(M)]
LIS2 = [[0 for i in range(M)] for j in range(M)]
LIS3 = [[[0 for i in range(M)] for j in range(M)] for k in range(M)]
for i in range(N-1):
    temp1 = [[[0 for _ in range(M)] for j in range(M)] for k in range(M)]
    for p in range(M-2):
        for q in range(p+1,M-1):
            for r in range(q+1,M):
                for s in range(p+1):
                    temp1[s][q][r]+=LIS3[p][q][r]
                    temp1[s][q][r]%=mod
                for s in range(p+1,q+1):
                    temp1[p][s][r]+=LIS3[p][q][r]
                    temp1[p][s][r]%=mod
                for s in range(q+1,r+1):
                    temp1[p][q][s]+=LIS3[p][q][r]
                    temp1[p][q][s]%=mod
    LIS3 = temp1.copy()              
    temp1 =[[0 for k in range(M)] for j in range(M)]
    for p in range(M-1):
        for q in range(p+1,M):
            for s in range(p+1):
                temp1[s][q]+=LIS2[p][q]
                temp1[s][q]%=mod
            for s in range(p+1,q+1):
                temp1[p][s]+=LIS2[p][q]
                temp1[p][s]%=mod
            for s in range(q+1,M):
                LIS3[p][q][s]+=LIS2[p][q]
                LIS3[p][q][s]%=mod
    LIS2 = temp1.copy()
    temp1 = [0 for k in range(M)]
    for t in range(M):
        for s in range(t+1):
            temp1[s]+=LIS1[t]
            temp1[s]%=mod
        for s in range(t+1,M):
            LIS2[t][s]+=LIS1[t]
            LIS2[t][s]%=mod
    LIS1 = temp1.copy()
ans = 0
for i in range(M-2):
    for j in range(i+1,M-1):
        for k in range(j+1,M):
            ans+=LIS3[i][j][k]
            ans%=mod
print(ans)



mod = 998244353
N,M = map(int,input().split())
from copy import copy
#p,q,rがそれぞれ1,2,3の長さの部分列になるような場合の数
LIS3 = [[[0 for i in range(M+1)] for j in range(M+1)] for k in range(M+1)]
LIS3[M][M][M]=1
for i in range(N):
    temp1 = [[[0 for _ in range(M+1)] for j in range(M+1)] for k in range(M+1)]
    for p in range(M+1):
        for q in range(p+1,M+1):
            for r in range(q+1,M+1):
                for s in range(p+1):
                    temp1[s][q][r]+=LIS3[p][q][r]
                    temp1[s][q][r]%=mod
                for s in range(p+1,q+1):
                    temp1[p][s][r]+=LIS3[p][q][r]
                    temp1[p][s][r]%=mod
                for s in range(q+1,r+1):
                    temp1[p][q][s]+=LIS3[p][q][r]
                    temp1[p][q][s]%=mod
    LIS3 = temp1.copy()
ans = 0
for i in range(M-2):
    for j in range(i+1,M-1):
        for k in range(j+1,M):
            ans+=LIS3[i][j][k]
            ans%=mod
print(ans)



