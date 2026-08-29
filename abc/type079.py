H,W = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
B = [list(map(int,input().split())) for i in range(H)]
ans = 0
for i in range(H-1):
    for j in range(W-1):
        dif = A[i][j]-B[i][j]
        ans += abs(dif)
        A[i][j]-=dif
        A[i+1][j]-=dif
        A[i][j+1]-=dif
        A[i+1][j+1]-=dif
for i in range(H-1):
    if A[i][W-1]!=B[i][W-1]:
        print("No")
        exit()
for j in range(W-1):
    if A[H-1][j]!=B[H-1][j]:
        print("No")
        exit()
print("Yes")
print(ans)
