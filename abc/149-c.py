N = int(input())
ans = [[0 for i in range(N)] for j in range(N)]
d = [1,2,6,4,5,3]
cnt = [0 for i in range(6)]
for i in range(N):
    for j in range(N):
        t = (i-j)%6
        ans[i][j]=cnt[t]*6+d[t]
        cnt[t]+=1
ans[2][1],ans[1][0]=ans[1][0],ans[2][1]
if N%6==2:
    ans[N-1][N-3]+=4
    ans[N-1][N-1]-=7
if N%6==3:
    ans[N-1][N-3]-=2
    ans[N-1][N-1]-=7
if N%6==4:
    ans[N-1][N-3]+=4
    ans[N-1][N-1]-=7
for i in range(N):
    print(*ans[i])