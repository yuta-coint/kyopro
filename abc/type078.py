N,M = map(int,input().split())
cnt = [0 for i in range(N+1)]
for i in range(M):
    a,b  = map(int,input().split())
    a-=1
    b-=1
    if a<b:
        cnt[b]+=1
    else:
        cnt[a]+=1
print(cnt.count(1))