import heapq
n,k = map(int,input().split())
s = input()
temp = []
s = [(s[i],i) for i in range(n)]
q = s[:n-k]
heapq.heapify(q)
ans = ""
used = -1
for i in range(n-k,n):
    heapq.heappush(q,s[i])
    while True:
        t = heapq.heappop(q)
        if t[1]>used:
            ans+=t[0]
            used = t[1]
            break
print(ans)  