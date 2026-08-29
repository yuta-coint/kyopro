N = int(input())
A = list(map(int,input().split()))
A.sort()
for i in range(N):
    if A[i]>=N-i:
        print(N-i)
        exit()
print(0)