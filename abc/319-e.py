#1から8までの最小公倍数は840なのでそいつらだけ調べる
N,X,Y = map(int,input().split())
bus = [tuple(map(int,input().split())) for i in range(N-1)]
ans = []
for start in range(840):
    time = start
    for i in range(N-1):
        p,t = bus[i]
        time = (1+(time-1)//p)*p
        time+=t
    ans.append(time)
Q = int(input())
for _ in range(Q):
    q = int(input())
    q+=X
    print(q-q%840+ans[q%840]+Y)