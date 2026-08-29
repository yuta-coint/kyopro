T= int(input())
from bisect import bisect_right
for _ in range(T):
    N = int(input())
    S = list(map(int,input().split()))
    goal = S[-1]
    now = S[0]
    ans = 2
    mae = -1
    S = S[1:N-1]
    S.sort()
    while True:
        if 2*now>=goal:
            break
        next = bisect_right(S,2*now)-1
        ans += 1
        if next == mae:
            ans = -1
            break
        now= S[next]
        mae = next
    print(ans)