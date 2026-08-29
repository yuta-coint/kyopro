N = int(input())
A = list(map(int,input().split()))
memo = [0 for i in range(N+1)]
cnt = [0 for i in range(N+1)]
ans = 0
for i in range(N):
    ans+=cnt[A[i]]*i-memo[A[i]]-(cnt[A[i]]*(cnt[A[i]]+1)//2)
    memo[A[i]]+=i
    cnt[A[i]]+=1
print(ans)