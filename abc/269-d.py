import sys
input = sys.stdin.readline
###コピペ
#再帰のおまじないを忘れずに
#size[find(a)]でaを含む連結成分の大きさを出力
n = 2002*2002
tree = [i for i in range(n)]
#size = [1 for i in range(n)]
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
N = int(input())
black = [tuple(map(int,input().split())) for i in range(N)]
def joint(s,t,u,v):
    if (u==s-1 and v==t-1) or (u==s-1 and v==t) or (u==s and v==t-1) or (u==s and v==t+1) or (u==s+1 and v==t) or (u==s+1 and v==t+1):
        return(True)
    else:
        return(False)

ans = N
for i in range(N):
    for j in range(i+1,N):
        if joint(black[i][0],black[i][1],black[j][0],black[j][1]):
            x,y,z,w = black[i][0]+1000,black[i][1]+1000,black[j][0]+1000,black[j][1]+1000
            if find(2002*x+y)!=find(2002*z+w):
                union(2002*x+y,2002*z+w)
                ans-=1
print(ans)

