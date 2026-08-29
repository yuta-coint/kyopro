N,K = map(int,input().split())
S = list(input())
cnt = 0
ans = 0
for i in range(N):
    if S[i]=="O":
        cnt+=1
    else:
        cnt=0
    if cnt == K:
        ans += 1
        cnt = 0
print(ans)