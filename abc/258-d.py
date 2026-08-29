N,X = map(int,input().split())
ab = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    ab.append(a+b)
    B.append(b)
ans= float('inf')
stage = 0
for i in range(1,N+1):
    if i>X:
        break
    stage+=ab[i-1]
    ans=min(ans,stage+B[i-1]*(X-i))
print(ans)

