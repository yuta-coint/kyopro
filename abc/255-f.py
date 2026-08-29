import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
P = list(map(lambda x:int(x)-1,input().split()))
I = list(map(lambda x:int(x)-1,input().split()))
rI = [0 for i in range(N)]
for i in range(N):
    rI[I[i]]=i
ansl = [-1 for i in range(N)]
ansr = [-1 for i in range(N)]
able = True
cnt = -1
#左側⇒右側の順番に調査する。l==rなら空間が無いことを報告する
#そうでないなら子供にどこが大丈夫か報告する
def dfs(l,r):
    if l==r:
        return(-1)
    global cnt
    global able
    cnt+=1
    #次に行きがけの順で訪れるやつが範囲に入っているか
    if not (l<=rI[P[cnt]]<r):
        able = False
        return(-1)
    c = P[cnt]
    ansl[c]=dfs(l,rI[c])
    ansr[c]=dfs(rI[c]+1,r)
    return(c)
dfs(0,N)
if P[0]!=0:
    able=False
if able:
    for i in range(N):
        print(ansl[i]+1,ansr[i]+1)
else:
    print(-1)
