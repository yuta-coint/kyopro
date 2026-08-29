import sys
input = sys.stdin.readline
N,X = map(int,input().split())
chk = [0 for i in range(X+1)]
chk[0]=1
base= 0
for i in range(N):
    a,b = map(int,input().split())
    base+=a
    c = b-a
    for j in reversed(range(c,X+1)):
        chk[j]=max(chk[j],chk[j-c])
if chk[X-base]==1:
    print("Yes")
else:
    print("No")
