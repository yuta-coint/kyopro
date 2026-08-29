N,M,T = map(int,input().split())
A = list(map(int,input().split()))
for i in range(M):
    x,y=  map(int,input().split())
    A[x-1]-=y
ans = "Yes"
for i in range(N-1):
    T-=A[i]
    if T<=0:
        ans="No"
print(ans)