import sys
input = sys.stdin.readline
n = int(input())
mi = 0
ma = 1<<60
baloon = []
for i in range(n):
    h,s = map(int,input().split())
    baloon.append([h,s])
while  ma>mi+1:
    time = [0 for i in range(n)]
    m = (ma+mi)//2
    for i in range(n):
        up = (m-baloon[i][0])//baloon[i][1]
        if up<0:
            time[0] = 2
            break
        elif up > n-1:
            time[n-1]+=1
        else:
            time[up]+=1
    safe = 1
    if time[0]>1:
        safe = 0
    for i in range(n-1):
        time[i+1] += time[i]
        if time[i+1]>i+2:
            safe = 0
            break
    if safe==1:
        ma = m
    else:
        mi = m
print(ma)