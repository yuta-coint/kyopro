N,K  = map(int,input().split())
S = input()
ans = ["x" for i in range(N)]
cnt = 0
for i in range(N):
    if S[i]=="o":
        ans[i]="o"
        cnt+=1
        if cnt==K:
            break
print(ans,sep="")