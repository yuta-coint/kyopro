N = int(input())
A = list(map(int,input().split()))
grundy = 0
for i in range(N):
    grundy ^= A[i]
if grundy == 0:
    print("Bob")
else:
    print("Alice")