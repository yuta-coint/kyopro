import sys
input = sys.stdin.readline
H,W = map(int,input().split())
###コピペ
#再帰のおまじないを忘れずに
#size[find(a)]でaを含む連結成分の大きさを出力
tree = [i for i in range(H*W)]
size = [1 for i in range(H*W)]
sys.setrecursionlimit(10**6)
def find(i):
    if tree[i] == i:
        return i
    else:
        tree[i]= find(tree[i])
        return find(tree[i])

def union(a,b):
    if tree[a] > tree[b]:
        a,b = b,a
    #以下二行が各成分のサイズの処理
    #if find(a)!=find(b):
    #    size[find(a)],size[find(b)]=size[find(b)]+size[find(a)],size[find(b)]+size[find(a)]
    tree[find(b)] = find(a)
S = [list(input()) for i in range(H)]
ans = 0
for i in range(H):
    ans+=S[i].count("#")
for i in range(H-1):
    for j in range(W):
        if S[i][j]=="#" and S[i+1][j]=="#":
            if find(i*W+j)!=find((i+1)*W+j):
                ans-=1
                union(i*W+j,(i+1)*W+j)

for i in range(H):
    for j in range(W-1):
        if S[i][j]=="#" and S[i][j+1]=="#":
            if find(i*W+j)!=find(i*W+j+1):
                ans-=1
                union(i*W+j,i*W+j+1)

for i in range(H-1):
    for j in range(W-1):
        if S[i][j]=="#" and S[i+1][j+1]=="#":
            if find(i*W+j)!=find((i+1)*W+j+1):
                ans-=1
                union(i*W+j,(i+1)*W+j+1)
        if S[i][j+1]=="#" and S[i+1][j]=="#":
            if find(i*W+j+1)!=find((i+1)*W+j):
                ans-=1
                union(i*W+j+1,(i+1)*W+j)
print(ans)