N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
emp = K
for i in range(N):
    if emp>=A[i]:
        emp-=A[i]
    else:
        ans+=1
        emp = K-A[i]
if emp!=K:
    ans+=1
print(ans)