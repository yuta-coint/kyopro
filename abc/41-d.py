import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dp = [0 for i in range(2**n)]
G = [[] for i in range(n)]
rG = [[] for i in range(n)]
for i in range(m):
    x,y = map(lambda x:int(x)-1,input().split())
    G[x].append(y)
    rG[y].append(x)
#立っているビットの分だけ並び替える方法
dp[0]=1
for i in range(1,2**n):
    #間に入らなきゃいけないもの
    ok = [True for _ in range(n)]
    for j in range(n):
        if i>>j & 1!=1:
            ok[j]=False
            continue
        for k in rG[j]:
            if i>>k & 1:
                ok[j]=False
                break
    for j in range(n):
        if ok[j]:
            dp[i]+=dp[i-2**j]
print(dp[-1])
            


