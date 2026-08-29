import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    ans = 0
    for i in range(1,10):
        for j in range(2,19):
            p = 0
            p10 = 1
            for k in range(j):
                p+=p10
                p10*=10**i
            if 10**(i-1)<=N//p:
                tri = min(10**i-1,N//p)
                ans = max(ans,tri*p)
    print(ans)

