def main():
    import sys
    input = sys.stdin.readline
    H,W = map(int,input().split())
    P = [list(map(int,input().split())) for _ in range(H)]
    ans = 0
    for bits in range(1,1<<H):
        cnt = [0 for _ in range(H*W+1)]
        for j in range(W):
            temp = []
            bk = 0
            for i in range(H):
                if (bits>>i)&1:
                    temp.append(P[i][j])
                    bk += 1
            if max(temp)==min(temp):
                cnt[min(temp)]+=1
        ans = max(ans,bk*max(cnt))
    print(ans)
main()

#A001913
N = int(input())
for i in range(1,N+1):
    temp=1
    if i%2==0 or i%5==0:
        print(i,"No")
        continue
    for j in range(i-2):
        temp*=10
        temp%=i
        if temp==1:
            print(i,"No")
            break
    else:
        print(i,"Yes")

N = int(input())
ans = []
G = [[] for i in range(N)]
from queue import Queue
start = Queue()
for i in range(N):
    a,b = map(int,input().split())
    G[a-1].append(i)
    G[b-1].append(i)
    if a-1==i or b-1==i:
        start.put(i)
check = [False for i in range(N)]
while not (start.empty()):
    k = start.get()
    if check[k]:
        continue
    check[k]=True
    ans.append(k)
    for i in G[k]:
        start.put(i)
ans.reverse()
if len(ans)==N:
    for i in range(N):
        print(ans[i]+1)
else:
    print(-1)