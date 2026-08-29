N=  int(input())
A = [list(input()) for i in range(N)]
ans = [[0 for i in range(N)] for j in range(N)]
for x in range(N):
    for y in range(N):
        time = min(N-x,N-y,x+1,y+1)
        if time%4==1:
            ans[y][N-x-1] = A[x][y]
        elif time%4==2:
            ans[N-x-1][N-y-1] = A[x][y]
        elif time%4==3:
            ans[N-y-1][x] = A[x][y]
        else:
            ans[x][y] = A[x][y]
for i in range(N):
    print(*ans[i],sep="")