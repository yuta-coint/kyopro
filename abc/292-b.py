N,Q = map(int,input().split())
players = [0 for i in range(N+1)]
for _ in range(Q):
    e,p = map(int,input().split())
    if e<3:
        players[p]+=e
    else:
        if players[p]>=2:
            print("Yes")
        else:
            print("No")
