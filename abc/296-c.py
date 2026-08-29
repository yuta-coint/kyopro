N,X = map(int,input().split())
A = list(map(int,input().split()))
sA = set(A)
for i in range(N):
    if A[i]+X in sA:
        print("Yes")
        break
else:
    print("No")