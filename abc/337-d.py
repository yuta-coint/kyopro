H,W,K = map(int,input().split())
grid = [input() for i in range(H)]
ans = 10**9
if K<=W:
    for i in range(H):
        cnto = 0
        cntx = 0
        for j in range(K):
            if grid[i][j]=="o":
                cnto +=1
            elif grid[i][j]=="x":
                cntx +=1
        if cntx==0 and (K-cnto<ans):
            ans = K-cnto
        for j in range(K,W):
            if grid[i][j]=="o":
                cnto +=1
            elif grid[i][j]=="x":
                cntx +=1
            if grid[i][j-K]=="o":
                cnto -=1
            elif grid[i][j-K]=="x":
                cntx -=1
            if cntx==0 and (K-cnto<ans):
                ans = K-cnto
if K<=H:
    for j in range(W):
        cnto = 0
        cntx = 0
        for i in range(K):
            if grid[i][j]=="o":
                cnto +=1
            elif grid[i][j]=="x":
                cntx +=1
        if cntx==0 and (K-cnto<ans):
            ans = K-cnto
        for i in range(K,H):
            if grid[i][j]=="o":
                cnto +=1
            elif grid[i][j]=="x":
                cntx +=1
            if grid[i-K][j]=="o":
                cnto -=1
            elif grid[i-K][j]=="x":
                cntx -=1
            if cntx==0 and (K-cnto<ans):
                ans = K-cnto
if ans == 10**9:
    print(-1)
else:
    print(ans)