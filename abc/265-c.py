import sys
input = sys.stdin.readline
H,W = map(int,input().split())
G = [list(input()) for _ in range(H)]
i = 0
j = 0
visited = set()
while True:
    if i*500+j in visited:
        ans = -1
        break
    visited.add(i*500+j)
    if G[i][j]=="U" and i!=0:
        i-=1
    elif G[i][j]=="D" and i!=H-1:
        i+=1
    elif G[i][j]=="L" and j!=0:
        j-=1
    elif G[i][j]=="R" and j!=W-1:
        j+=1
    else:
        ans=(i+1,j+1)
        break
if ans==-1:
    print(ans)
else:
    print(*ans)
