N,X,K = map(int,input().split())
colors = [[] for i in range(N)]
for i in range(N):
    p,u,c = map(int,input().split())
    colors[c-1].append((p,u))
kouyou_max = [0 for i in range(X+1)]
for i in range(N):
    #一個以上購入した場合の数値が書き込まれているか
    next_color = [0 for i in range(X+1)]
    for p,u in colors[i]:
        for j in reversed(range(p,X+1)):
            c=0
            #2個目以降の購入
            if next_color[j]<next_color[j-p]+u:
                next_color[j]=next_color[j-p]+u
            #1個目の購入
            if next_color[j]<kouyou_max[j-p]+u+K:
                next_color[j]=kouyou_max[j-p]+u+K
    for j in range(X+1):
        kouyou_max[j] = max(kouyou_max[j],next_color[j])
print(max(kouyou_max))