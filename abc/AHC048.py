def dst(p,q):
    r = 0
    for i in range(3):
        r+=(p[i]-q[i])**2
    return r
N,K,H,T,D = map(int,input().split())
ingredient = [tuple(map(float,input().split())) for i in range(K)]

for i in range(N):
    print(*[1 for j in range(N-1)])
for i in range(N-1):
    print(*[1 for j in range(N)])
for _ in range(H):
    c = tuple(map(float,input().split()))
    tmp,mi = 0,100
    for i in range(K):
        if dst(c,ingredient[i])<mi:
            mi = dst(c,ingredient[i])
            tmp = i
    print(1,0,0,tmp)
    print(2,0,0)