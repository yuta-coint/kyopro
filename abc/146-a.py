N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
pqr = [str(A[0]),str(A[1]),str(A[2])]
ans = 0
for q in ([0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]):
    ans = max(ans,int(pqr[q[0]]+pqr[q[1]]+pqr[q[2]]))
print(ans)
