N,M = map(int,input().split())
S=[list(input()) for i in range(N)]
ans = 0
for x in range(N-1):
    for y in range(x+1,N):
        for q in range(M):
            if S[x][q]=="x" and S[y][q]=="x":
                break
        else:
            ans+=1
print(ans)