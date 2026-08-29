N,Q = map(int,input().split())
rans = [i for i in range(N+1)]
ans = [i for i in range(N+1)]
right = N
rr = N-1
for i in range(Q):
    x=int(input())
    rx = rans[x]
    if rx==N:
        rx-=1
    rans[ans[rx]],rans[ans[rx+1]]=rans[ans[rx+1]],rans[ans[rx]]
    ans[rx],ans[rx+1]=ans[rx+1],ans[rx]
print(*ans[1:])

N,A,B = map(int,input().split())
ans = [["." for j in range(B*N)] for i in range(A*N)]
for i in range(A*N):
    for j in range(B*N):
        if ((i//A)+(j//B))%2==1:
            ans[i][j]="#"
for i in range(A*N):
    print(*ans[i],sep="")
H,W = map(int,input().split())
R,C = map(int,input().split())
ans = 4
if R==1 or R==H:
    ans-=1
if H==1:
    ans-=1
if C==1 or C==W:
    ans-=1
if W == 1:
    ans-=1
print(ans)
            
            