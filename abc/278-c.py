import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
d = {}
for i in range(Q):
    T,A,B = map(int,input().split())
    if T==1:
        d[A,B]=1
    elif T==2:
        d[A,B]=0
    else:
        ans = "No"
        if (A,B) in d and (B,A) in d:
            if d[A,B]==1 and d[B,A]==1:
                ans="Yes"
        print(ans)