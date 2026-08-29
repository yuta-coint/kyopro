p = 23
ans = [[-1 for j in range(p*p)] for i in range(p*p)]
for i in range(p):
    for j in range(p):
        for k in range(p):
            for l in range(p):
                ans[p*i+j][p*k+l] = (i+j*k+l)%p+1
N,M = map(int,input().split())
for i in range(N):
    print(*ans[i][:M])