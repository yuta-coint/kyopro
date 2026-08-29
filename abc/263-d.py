N,L,R  = map(int,input().split())
A = list(map(int,input().split()))
Lans = [0 for i in range(N+1)]
ans = R*N
for i in range(1,N+1):
    Lans[i] = min(L*i,Lans[i-1]+A[i-1])
    ans = min(ans,Lans[i]+(N-i)*R)
print(ans)