N,M,K = map(int,input().split())
roots = [[]]+[tuple(map(int,input().split())) for i in range(M)]
E = list(map(int,input().split()))
short = [float("inf") for i in range(N+1)]
short[1]=0
for i in range(K):
    #print(roots)
    A,B,C = roots[E[i]][0],roots[E[i]][1],roots[E[i]][2]
    if short[A]!=float("inf"):
        if short[A]+C<short[B]:
            short[B]=short[A]+C
if short[N]==float("inf"):
    print(-1)
else:
    print(short[N])
