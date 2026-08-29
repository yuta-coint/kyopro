board = [input() for i in range(8)]
safe = [[1 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        if board[i][j]=="#":
            for k in range(8):
                safe[i][k]=0
                safe[k][j]=0
ans = 0
for i in range(8):
    ans+=sum(safe[i])
print(ans)