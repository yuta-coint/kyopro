import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
Q = int(input())
d = {}
ma = 0
mi = 10**9+1
from heapq import heapify,heappop,heappush
numbers = []
numbers2 = []
heapify(numbers)
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0]==1:
        x = query[1]
        if x in d:
            d[x]+=1
        else:
            d[x]=1
        heappush(numbers,x)
        heappush(numbers2,-x)
    elif query[0]==2:
        x,c = query[1],query[2]
        if x in d:
            d[x]=max(0,d[x]-c)
    else:
        while True:
            k = heappop(numbers)
            if d[k]==0:
                continue
            else:
                mi = k
                heappush(numbers,k)
                break
        while True:
            k = heappop(numbers2)
            if d[-k]==0:
                continue
            else:
                ma = -k
                heappush(numbers2,k)
                break
        print(ma-mi)