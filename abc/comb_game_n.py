
T = int(input())
for _ in range(T):
    N = int(input())
    l = 0
    ans = "Bob"
    for i in range(N):
        A,B = map(int,input().split())
        if A%(B + 1) == 0:
            l^= A//(B+1)
        else:
            ans = "Alice"
    if l != 0:
        ans = "Alice"
    print(ans)