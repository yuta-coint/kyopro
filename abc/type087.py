v,P,K = map(int,input().split())
A = [list(map(int,input().split())) for i in range(v)]
def WF(X):
    #length[i][j]はiからjへの長さ。有向グラフを前提に書かれている
    length = [["INF" for i in range(v)] for j in range(v)]
    for i in range(v):
        for j in range(v):
            if A[i][j]==-1:
                length[i][j]=X
            else:
                length[i][j]=A[i][j]
    for i in range(v):
        for j in range(v):
            for k in range(v):
                if length[j][k]>length[j][i]+length[i][k]:
                    length[j][k]=length[j][i]+length[i][k]
    near_towns = 0
    for i in range(v):
        for j in range(i+1,v):
            if length[i][j]<=P:
                near_towns+=1
    return near_towns
#K+1以上に収まるXの最大値を求める
ok = 0
ng = 10**10
while ok+1<ng:
    ma = (ok+ng)//2
    if WF(ma)>=K+1:
        ok = ma
    else:
        ng = ma
ma = ok
#K以上に収まるXの最大値を求める
ok = 0
ng = 10**10
while ok+1<ng:
    mi = (ok+ng)//2
    if WF(mi)>=K:
        ok = mi
    else:
        ng = mi
mi = ok
if mi == 10**10-1 and ma!=10**10-1:
    print("Infinity")
else:
    print(mi-ma)