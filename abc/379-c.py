N,M = map(int,input().split())
X = list(map(int,input().split()))
A = list(map(int,input().split()))
if sum(A)!=N:
    print(-1)
    exit()
stones = [(X[i]-1,A[i]) for i in range(M)]
stones.sort()
if stones[0][0]!=0:
    print(-1)
    exit()
stones.append((N,0))
lack = 0
for i in reversed(range(M)):
    x,a = stones[i]
    lack += stones[i+1][0]-x
    if lack<a:
        print(-1)
        exit()
    else:
        lack-=a
if lack>0:
    print(-1)
    exit()
ans = 0
for i in range(M):
    ans += stones[i][0]*stones[i][1]
ans = (N*(N-1)//2)-ans
print(ans)