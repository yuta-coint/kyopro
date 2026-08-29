N = int(input())
A = [list(map(int,input().split())) for i in range(N)]
def circ(A):
    new = [[A[N-j-1][i] for j in range(N)] for i in range(N)]
    return(new)
B = [list(map(int,input().split())) for i in range(N)]

for i in range(4):
    A = circ(A)
    ans = True
    for i in range(N):
        for j in range(N):
            if A[i][j]>B[i][j]:
                ans = False
    if ans:
        print("Yes")
        break
else:
    print("No")
