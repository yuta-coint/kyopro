T = int(input())
for case in range(T):
    N = int(input())
    G = [[] for i in range(N)]
    for i in range(N-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    S = list(input())
    ans = [-1 for i in range(N)]
    parent = [-1 for i in range(N)]
    is_bottom = [False for i in range(N)]
    def backward(n, X, i0):
        done = [0] * n
        Q = [-i0-1, i0] # 根をスタックに追加
        bw = []
        while Q:
            i = Q.pop()
            if i >= 0: # 行きがけの処理
                done[i] = 1
                bottom = True
                for a in X[i][::-1]:
                    if done[a]: continue
                    parent[a]=i
                    Q.append(~a) # 帰りがけの処理をスタックに追加
                    Q.append(a) # 行きがけの処理をスタックに追加
                    bottom =False
                if bottom:
                    is_bottom[i]=True
            else: # 帰りがけの処理
                bw.append(~i)
        bw.pop()
        return bw
    flag = 0
    bwd = backward(N,G,0)
    for i in bwd:
        if ans[i]==-1:
            ans[i]=S[parent[i]]
        win = 0
        lose = 0
        for j in G[i]:
            if j==parent[i]:
                continue
            if S[i]==ans[j]:
                win+=1
            else:
                lose+=1
        if win==lose:
            if ans[parent[i]]==-1 or ans[parent[i]]==S[i]:
                ans[parent[i]]=S[i]
            else:
                flag = 1
                break
        elif win<lose:
            flag=1
            break
    if flag==1:
        print(-1)
        continue
    if ans[0]==-1:
        ans[0]="B"
    win = 0
    lose =0
    for j in G[0]:
        if S[0]==ans[j]:
            win+=1
        else:
            lose+=1
    if win<lose:
        print(-1)
        continue
    print(*ans,sep="")