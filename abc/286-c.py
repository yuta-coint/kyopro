N,A,B=map(int,input().split())
S = list(input())
ans =float('inf')
for t in range(N):
    cost =  t*A
    for i in range(N//2):
        if S[i]!=S[N-1-i]:
            cost+=B
    if cost<ans:
        ans = cost
    S = S[1:]+S[:1]
print(ans)
