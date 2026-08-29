H,W =map(int,input().split())
board = [list(input()) for i in range(H)]
ans = "Yes"
for i in range(H):
    for j in range(W):
        if board[i][j] == ".":
            continue
        cnt= 0
        if i > 0:
            if board[i-1][j] == "#":
                cnt += 1
        if j > 0:
            if board[i][j-1] == "#":
                cnt += 1
        if i < H-1:
            if board[i+1][j] == "#":
                cnt += 1
        if j < W - 1:
            if board[i][j+1] == "#":
                cnt += 1
        if cnt == 2 or cnt == 4:
            continue
        ans = "No"
print(ans)
            
            