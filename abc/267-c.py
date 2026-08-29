N,M = map(int,input().split())
A = list(map(int,input().split()))
temp = 0
for i in range(M):
    temp+=A[i]*(i+1)
s = 0
s = sum(A[:M])
ans = temp
for i in range(M,N):
    temp-=s
    temp+=A[i]*M
    s+=A[i]
    s-=A[i-M]
    ans =max(ans,temp)
print(ans)