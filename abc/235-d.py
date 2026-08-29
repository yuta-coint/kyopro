import sys
sys.setrecursionlimit(10**6)
import queue
q = queue.Queue()
a,n = map(int,input().split())
check = [0 for i in range(10**6)]
length = [float('inf') for i in range(10**6)]
q.put(1)
length[1]=0
check[1]=1
while not q.empty():
    i=q.get()
    l = len(str(i))
    if i*a<10**6:
        if check[i*a]==0:
            check[i*a]=1
            q.put(i*a)
            length[i*a]=length[i]+1
    if i>=10 and i%10!=0:
        k=(i%10)*(10**(l-1))+(i//10)
        if check[k]==0:
            check[k]=1
            length[k]=length[i]+1
            q.put(k)
if length[n]==float('inf'):
    print(-1)
else:
    print(length[n])