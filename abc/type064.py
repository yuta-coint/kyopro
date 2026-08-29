N,Q  = map(int,input().split())
A = list(map(int,input().split()))
sA = []
for i in range(1,N):
    sA.append(A[i]-A[i-1])
ans = 0
for i in range(1,N):
    ans += abs(A[i]-A[i-1]) 
for _ in range(Q):
    L,R,V = map(int,input().split())
    if L>1:
        ans+=abs(sA[L-2]+V)-abs(sA[L-2])
        sA[L-2]+=V
    if R<N:
        ans+=abs(sA[R-1]-V)-abs(sA[R-1])
        sA[R-1]-=V
    print(ans)
