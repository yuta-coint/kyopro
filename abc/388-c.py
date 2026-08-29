N = int(input())
A = list(map(int,input().split()))
l = 0
ans = 0
for i in range(N):
    while l<N:
        if A[l]<=A[i]//2:
            l+=1
        else:
            break
    ans += l
print(ans)