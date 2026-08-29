N = int(input())
K = [list(map(int,input().split())) for i in range(N)]
chk = [{} for i in range(N)]
for i in range(N):
    for k in range(1,1+K[i][0]):
        if K[i][k] in chk[i]:
            chk[i][K[i][k]]+=1
        else:
            chk[i][K[i][k]]=1
#print(chk)
ans = 0
for i in range(N):
    for j in range(i+1,N):
        cnt = 0
        for k in range(1,K[i][0]+1):
            t = K[i][k]
            if t in chk[j]:
                cnt+=chk[j][t]
        if cnt/(K[i][0]*K[j][0])>ans:
            ans = cnt/(K[i][0]*K[j][0])
print(ans)