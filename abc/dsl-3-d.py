#https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D
#スライド最小値K…数列の長さL…windowの大きさa…数列
from collections import deque
K,L = map(int,input().split())
a = list(map(int,input().split()))
window = deque([])
r = (a[0],0)
ans = []
for i in range(K):
    f = 0
    if window:
        r=window.pop()
        f = 1
    while r[0]>a[i] and window:
        r=window.pop()
    if (r[0]<=a[i] or i==0) and f==1:
        window.append(r)
    window.append((a[i],i))
    if i<L-1:
        continue
    ans.append(window[0][0])
    if window[0][1]<=i+1-L:
        window.popleft()
print(*ans)

def Sliding_mimimum_elements(K,L,a):
    window = deque([])
    r = (a[0],0)
    ans = []
    #どこの値かの復元
    ind = []
    for i in range(K):
        f = 0
        if window:
            r=window.pop()
            f = 1
        while r[0]>a[i] and window:
            r=window.pop()
        if (r[0]<=a[i] or i==0) and f==1:
            window.append(r)
        window.append((a[i],i))
        if i<L-1:
            continue
        ans.append(window[0][0])
        ind.append(window[0][1])
        if window[0][1]<=i+1-L:
            window.popleft()
    return ans