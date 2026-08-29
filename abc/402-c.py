N,M = map(int,input().split())
kirai = [[] for i in range(N)]
cnt = []
for i in range(M):
    K = list(map(int,input().split()))
    cnt.append(K[0])
    for j in range(1,K[0]+1):
        kirai[K[j]-1].append(i)
B =  list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in kirai[B[i]-1]:
        cnt[j]-=1
        if cnt[j]==0:
            ans+=1
    print(ans)