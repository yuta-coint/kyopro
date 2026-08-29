N,Q = map(int,input().split())
d = {i:i for i in range(N)}
#単純にその番号の辺の次数をカウントしている
counting = [0 for i in range(N)]
new  =N
check = [[] for i in range(N+Q)]
rd = {i:i for i in range(N)}
ans = N
broken = set()
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0]==1:
        u,v = query[1]-1,query[2]-1
        #新しくゼロが消えていないか？
        if counting[u]==0:
            ans-=1
        if counting[v]==0:
            ans-=1
        counting[u]+=1
        counting[v]+=1
        check[d[u]].append(d[v])
        check[d[v]].append(d[u])
    else:
        v = query[1]-1
        broken.add(d[v])
        if counting[v]>0:
            ans+=1
        for u in check[d[v]]:
            if u in broken:
                continue
            counting[rd[u]]-=1
            if counting[rd[u]]==0:
                ans+=1
        d[v]=new
        rd[new]=v
        new+=1
        counting[v]=0
    print(ans)