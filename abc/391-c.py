N,Q = map(int,input().split())
pigeon = [i for i in range(N)]
cnt = [1 for i in range(N)]
ans = 0
for q in range(Q):
    query = list(map(int,input().split()))
    if query[0]==1:
        query[1]-=1
        query[2]-=1
        cnt[pigeon[query[1]]]-=1
        if cnt[pigeon[query[1]]]==1:
            ans -=1
        pigeon[query[1]] = query[2]
        cnt[pigeon[query[1]]]+=1
        if cnt[pigeon[query[1]]]==2:
            ans +=1
    else:
        print(ans)