N = int(input())
A = list(map(int,input().split()))
A = [(A[i],i) for i in range(N)]
ans = [0 for i in range(N)]
A.sort(reverse=True)
sumA = [0]
for i in range(N):
    sumA.append(sumA[-1]+A[i][0])
temp = -1
for i in range(N):
    if i==0:
        temp = sumA[0]
    elif A[i][0]<A[i-1][0]:
        temp = sumA[i]
    ans[A[i][1]] = temp
print(*ans)