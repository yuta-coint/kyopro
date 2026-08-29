N,P,Q,R = map(int,input().split())
A = list(map(int,input().split()))
sA = [0]
for i in range(N):
    sA.append(sA[-1]+A[i])
ssA = set(sA)
ans = "No"
for i in range(N):
    if sA[i]+P in ssA and sA[i]+P+Q in ssA and sA[i]+P+Q+R in ssA:
        ans = "Yes"
print(ans)