import bisect
from operator import indexOf
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
rq = [0 for i in range(n+1)]
for i in range(n):
    rq[q[i]]=i
rp = [[] for i in range(n)]
for i in range(n):
    for j in range(1,(n//p[i])+1):
        rp[i].append(rq[p[i]*j])
for i in range(n):
    rp[i].sort(reverse=True)
LIS = [-1]
for i in range(n):
    flag = 0
    for a in rp[i]:
        if a > LIS[-1]:
            LIS.append(a)
        else:
            LIS[bisect.bisect_left(LIS, a)] = a
print(len(LIS)-1)