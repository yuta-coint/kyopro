N = int(input())
c = N//2
ans = [[0 for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if i+j>2*c and i-j>0:
            ans[i][j] = (2*(i-c))**2-(i-j)
        elif i+j<=2*c and i-j>0:
            ans[i][j] = (2*(c-j)-1)**2+i-j-1
        elif i+j>2*c and i-j<=0:
            ans[i][j] = (2*(j-c))**2+(j-i)
        elif i+j<=2*c and i-j<=0:
            ans[i][j] = (2*(c-i)+1)**2+i-j-1
ans[c][c]="T"
for i in range(N):
    print(*ans[i])