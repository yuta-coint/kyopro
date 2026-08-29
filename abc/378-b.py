N=int(input())
schedule = [tuple(map(int,input().split())) for i in range(N)]
Q = int(input())
for _ in range(Q):
    t,d = map(int,input().split())
    q,r = schedule[t-1]
    #d以上で、qで割ってr余る最小の数
    if d%q == r:
        print(d)
    else:
        print((((d-r)//q)+1)*q+r)