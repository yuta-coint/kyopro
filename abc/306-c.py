N = int(input())
appear = [0 for i in range(N+1)]
A = list(map(int,input().split()))
ans = []
for i in range(3*N):
    appear[A[i]]+=1
    if appear[A[i]]==2:
        ans.append(A[i])
print(*ans)