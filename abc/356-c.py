N,M,K = map(int,input().split())
key = [list(input().split()) for i in range(M)]
ans = 0
for pat in range(1<<N):
    chk = 1
    for i in range(M):
        cnt = 0
        for j in range(1,int(key[i][0])+1):
            cnt+=(pat>>(int(key[i][j])-1))&1
        if cnt>=K and key[i][-1]=="x":
            chk=0
            break
        if cnt<K and key[i][-1]=="o":
            chk=0
            break
    ans+=chk
print(ans)