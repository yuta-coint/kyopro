T = int(input())
for case in range(T):
    N = int(input())
    P = list(map(int,input().split()))
    mi = 10**9
    ans = 0
    for i in reversed(range(N)):
        if P[i]<mi:
            mi = P[i]
            ans+=1
    print(ans)