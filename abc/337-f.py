N,M,K = map(int,input().split())
C = list(map(int,input().split()))
d = {i:0 for i in range(1,N+1)}
ind = [[10**9] for i in range(N+1)]
cnt_color = 0
for i in reversed(range(N)):
    if d[C[i]]==0:
        cnt_color+=1
    if d[C[i]]<K:
        d[C[i]]+=1
    ind[C[i]].append(i+N)
for i in reversed(range(N)):
    ind[C[i]].append(i)
ans = 0
if cnt_color<M:
    for i in range(1,N+1):
        ans += d[i]
    for i in range(N):
        print(ans)
    exit()        
from heapq import heapify,heappop,heappush
cand = [(ind[i].pop(),i) for i in range(N+1)]
heapify(cand)
#採択していき、直ちに次点を流し込みたいところだが、既出のものを回収しても虚無になるんだよな。
#カットされた瞬間次点を流し込めばいいのか
#色がM色以上あるものと考えよう
for i in range(M):
    p,c = heappop(cand)
    #print(p,c)
    ans += d[c]
print(ans)
#先頭の色をカットする
for r in range(N-1):
    ans-=d[C[r]]
    heappush(cand,(ind[C[r]].pop(),C[r]))
    p,c = heappop(cand)
    ans += d[c]
    print(ans)