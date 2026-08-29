N = int(input())
A = list(map(int,input().split()))
A.sort()
ave = sum(A)//N
sa = sum(A)%N
ideal = [ave for i in range(N-sa)]+[ave+1 for i in range(sa)]
ans = 0
for i in range(N):
    if ideal[i]>A[i]:
        ans+=ideal[i]-A[i]
print(ans)