import sys
input = sys.stdin.readline
n = int(input())
size = [[] for i in range(10**5)]
for i in range(n):
    w,h =map(int,input().split())
    size[w-1].append(h-1)
LIS = [-1]
import bisect
for i in range(10**5):
    temp = []
    add = []
    for ww in size[i]:
        if ww>LIS[-1]:
            add.append(ww)
        else:
            p = bisect.bisect_left(LIS, ww)
            temp.append([ww,p])
    if add!=[]:
        LIS.append(min(add))
    for q in temp:
        LIS[q[1]]=min(q[0],LIS[q[1]])
print(len(LIS)-1)