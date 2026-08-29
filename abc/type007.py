from bisect import bisect_left as bl
n = int(input())
a = list(map(int,input().split()))
q = int(input())
a.sort()
for i in range(q):
    b = int(input())
    cla = bl(a,b)
    if cla == 0:
        print(a[0]-b)
    elif cla == n:
        print(b-a[n-1])
    else:
        print(min(b-a[cla-1],a[cla]-b))