N = int(input())
Si = [(input(),i) for i in range(N)]
Si.sort()
S = [Si[i][0] for i in range(N)]
ls = [len(S[i]) for i in range(N)]
ans = [0 for i in range(N)]
for i in range(N-1):
    lenl = len(S[i])
    lenr = len(S[i+1])
    mlr = min(lenl,lenr)
    temp = mlr
    for j in range(mlr):
        if S[i][j]!=S[i+1][j]:
            temp=j
            break
    ans[Si[i][1]] = max(ans[Si[i][1]],temp)
    ans[Si[i+1][1]] = max(ans[Si[i+1][1]],temp)
for i in range(N):
    print(ans[i])
    
