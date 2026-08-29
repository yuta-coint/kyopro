#お互い大丈夫な組み合わせから取っていく
N = int(input())
A = [list(map(lambda x:int(x)-1,input().split())) for i in range(N)]
finished = 0
players = [0 for i in range(N)]
#iがjと対戦する準備ができているか
ready = [[False for j in range(N)] for i in range(N)]
S = set()
new = []
for i in range(N):
    S.add(i*N+A[i][0])
    new.append((i,A[i][0]))
ans = 0
while True:
    #一通り新しいのを確認する
    today = set()
    for p,q in new:
        if p*N+q in S and q*N+p in S:
            today.add(p)
            today.add(q)
    if not today:
        break
    ans+=1
    new = []
    for p in today:
        players[p]+=1
        if players[p]==N-1:
            finished+=1
            continue
        S.add(p*N+A[p][players[p]])
        new.append((p,A[p][players[p]]))
if finished==N:
    print(ans)
else:
    print(-1)

