import sys
input = sys.stdin.readline
n,q =  map(int,input().split())
base = -1
a = list(map(int,input().split()))
sa = sum(a)
a = [(a[i],-1) for i in range(n)]
now = -1
for t in range(q):
    qu = list(map(int,input().split()))
    if qu[0]==2:
        base = qu[1]
        print(qu[1]*n)
        now = t
        sa = qu[1]*n
    else:
        i,x = qu[1]-1,qu[2]
        if a[i][1]==now:
            sa +=x
            sa-=a[i][0]
        else:
            sa+=x
            sa-=base
        a[i]=(x,now)
        print(sa)