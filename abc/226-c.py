N = int(input())
wepons = [[]]+[list(map(int,input().split())) for i in range(N)]
chk = [False for i in range(N+1)]
ans = 0
chk[N]=True
#print(wepons)
for i in reversed(range(1,N+1)):
    if chk[i]==False:
        continue
    T,K,A = wepons[i][0],wepons[i][1],wepons[i][2:]
    ans+=T
    for a in A:
        chk[a]=True
print(ans)
