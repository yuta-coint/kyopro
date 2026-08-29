N,M,A,B = map(int,input().split())
X = list(map(int,input().split()))
if A<=B:
    print(N)
    exit()
cnt = [0 for i in range(N)]
for i in range(M):
    cnt[X[i]-1]+=1
cnt.sort()
attack = A-B
for i in range(N):
    if B>=cnt[i]:
        B-=cnt[i]
        cnt[i]=0
    else:
        break
print(max(cnt.count(0),N-attack))