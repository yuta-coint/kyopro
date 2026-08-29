N = int(input())
A = list(map(int,input().split()))
P = [0]+list(map(lambda x:int(x)-1,input().split()))
dist = [0]
for i in range(1,N):
    dist.append(dist[P[i]]+1)
#print(dist)
cnt = [0 for i in range(N)]
for i in range(N):
    cnt[dist[i]]+=A[i]
ans = 0
for i in reversed(range(N)):
    if cnt[i]>0:
        ans = "+"
        break
    if cnt[i]<0:
        ans = "-"
        break
print(ans)