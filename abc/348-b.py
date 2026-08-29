N = int(input())
points = [tuple(map(int,input().split())) for i in range(N)]
d = [[(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2 for j in range(N)] for i in range(N)]
for i in range(N):
    ans = N-1
    ma = 0
    for j in reversed(range(N)):
        if ma<=d[i][j]:
            ma = d[i][j]
            ans = j
    print(ans+1)