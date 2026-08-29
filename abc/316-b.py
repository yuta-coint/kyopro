N = int(input())
A = list(map(int,input().split()))
mi = min(A)
for i in range(N):
    A[i]-=mi
for i in range(N+1):
    if i in A:
        continue
    print(i+mi)
    exit()