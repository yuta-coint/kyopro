N,K,Q  =map(int,input().split())
A = list(map(int,input().split()))
L = list(map(int,input().split()))
for i in range(Q):
    if L[i]==K:
        A[K-1]=min(A[K-1]+1,N)
    elif A[L[i]-1]+1==A[L[i]]:
        continue
    else:
        A[L[i]-1]+=1
print(*A)