N = int(input())
S = [input() for i in range(N)]
cnt = [0 for i in range(N)]
cnt2 = [0 for i in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j]=="o":
            cnt[i]+=1
            cnt2[j]+=1
ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j]=="o":
            ans += (cnt[i]-1)*(cnt2[j]-1)
print(ans)