import sys
input = sys.stdin.readline
n = 1<<20
a = [None for i in range(n)]
count = [i for i in range(n)]
q = int(input())
for i in range(q):
    t,x = map(int,input().split())
    k = x
    if t == 1:
        while True:
            if count[k%n]==k%n:
                break
            else:
                k=count[k%n]
        a[k%n]=x
        count[k%n]=(k+1)%n
        count[x%n]=(k+1)%n
    else:
        if a[x%n]==None:
            print(-1)
        else:
            print(a[x%n])