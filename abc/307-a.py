N=int(input())
A = list(map(int,input().split()))
print(*[sum(A[7*i:7*(i+1)]) for i in range(N)])