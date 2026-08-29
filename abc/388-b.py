N,D = map(int,input().split())
snake = [tuple(map(int,input().split())) for i in range(N)]
for k in range(1,D+1):
    ans = 0
    for T,L in snake:
        weight = T*(L+k)
        if weight >ans:
            ans = weight
    print(ans)