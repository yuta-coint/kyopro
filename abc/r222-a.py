T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    width = 1
    for i in range(M):
        l,r = map(int,input().split())
        if r - l + 1 > width:
            width = r - l + 1
    ans = [(i%width) + 1 for i in range(N)]
    print(*ans)