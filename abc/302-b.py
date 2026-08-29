H,W = map(int,input().split())
S = [list(input()) for i in range(H)]
plus = [(0,1),(0,-1),(1,-1),(1,0),(1,1),(-1,-1),(-1,0),(-1,1)]
snuke = "snuke"
for i in range(H):
    for j in range(W):
        for p in plus:
            for t in range(5):
                if not (0<=i+p[0]*t<H and 0<=j+p[1]*t<W):
                    break
                if S[i+p[0]*t][j+p[1]*t]!=snuke[t]:
                    break
            else:
                for t in range(5):
                    print(i+p[0]*t+1,j+p[1]*t+1)
                exit()