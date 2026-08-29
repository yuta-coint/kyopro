N,M = map(int,input().split())
cand = [1 for i in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    cand[B-1]=0
if sum(cand)==1:
    print(cand.index(1)+1)
else:
    print(-1)