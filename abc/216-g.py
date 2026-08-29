#RSQ
def add(i,x):
    while i<=n:
        BIT[i]+=x
        i += (i&-i)
#xまでの和をとる
def getSum(x):
    i = x
    gs = 0
    while i>0:
        gs+=BIT[i]
        i -= (i&-i)
    return(gs)
import queue
import sys
input = sys.stdin.readline

q = queue.LifoQueue()
n,m = map(int,input().split())
BIT = [0 for i in range(n+1)]
que = []
for i in range(m):
    l,r,x = map(int,input().split())
    que.append([r,l,x])
que.sort()
cnt = 0
for t in que:
    while cnt<=t[0]:
        q.put(cnt)
        cnt+=1
    rem = getSum(t[0])-getSum(t[1]-1)
    if rem>=t[2]:
        continue
    for i in range(t[2]-rem):
        a = q.get()
        add(a,1)
anssum = []
for i in range(n+1):
    anssum.append(getSum(i))
ans = []
for i in range(1,n+1):
    ans.append(anssum[i]-anssum[i-1])
print(*ans)