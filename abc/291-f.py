N,M = map(int,input().split())
INF = 10**9
S = [list(input()) for i in range(N)]
dp_start = [INF for i in range(N)]
dp_start[0]=0
for i in range(N):
    for stride in range(1,M+1):
        if S[i][stride-1]=="0":
            continue
        if dp_start[i+stride]>dp_start[i]+1:
            dp_start[i+stride]=dp_start[i]+1
dp_goal = [INF for i in range(N)]
dp_goal[N-1]=0
for i in reversed(range(N-1)):
    for stride in range(1,M+1):
        if S[i][stride-1]=="0":
            continue
        if dp_goal[i]>dp_goal[i+stride]+1:
            dp_goal[i]=dp_goal[i+stride]+1
#print(dp_start)
#print(dp_goal)
ans = [INF for i in range(N)]
for i in range(N):
    for stride in range(1,1+M):
        if S[i][stride-1]=="0":
            continue
        for k in range(i+1,i+stride):
            if ans[k]>dp_start[i]+dp_goal[i+stride]+1:
                ans[k]=dp_start[i]+dp_goal[i+stride]+1
p = []
for i in range(1,N-1):
    if ans[i]==INF:
        p.append(-1)
    else:
        p.append(ans[i])
print(*p)
