import sys
input = sys.stdin.readline
v, e = map(int,input().split())
#length[j][k]はiからjへの長さ。有向グラフを前提に書かれている
#iからjに行けるか？経由する頂点を一つづつ開放していく
length = [0 for i in range(v)]
G = [[]for i in range(v)]
for i in range(v):
    length[i]+=1<<i
for i in range(e):
    a,b = map(lambda x:int(x)-1,input().split())
    length[a]+=1<<(b)
Q = int(input())
st = [tuple(map(lambda x:int(x)-1,input().split())) for i in range(Q)]
ans = [v for i in range(Q)]
for i in range(v):
    for j in range(v):
         #jからiへのパスがあるならjからkへのパスをiからkへのパスとのorに
         if (length[j]>>i)&1:
             length[j]|=length[i]
    #i以下の頂点だけでパスが完成しているか否か
    for j in range(Q):
        s,t = st[j]
        if i<s or i<t:
            continue
        if (length[s]>>t)&1 and ans[j]==v:
            ans[j]=i
for i in range(Q):
    if ans[i]==v:
        print(-1)
    else:
        print(ans[i]+1)