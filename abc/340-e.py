N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
#RSQ
n = N+2
#n:数列の長さ
BIT = [0 for i in range(n+1)]
def add(i,x):
    i+=1
    while i<=n:
        BIT[i]+=x
        i += (i&-i)
#xまでの和をとる
def getSum(x):
    x+=1
    i = x
    gs = 0
    while i>0:
        gs+=BIT[i]
        i -= (i&-i)
    return gs
pre = 0
for i in range(N):
    add(i,A[i]-pre)
    pre = A[i]
for i in range(M):
    #ボールを全て取り出す。
    hand = getSum(B[i])
    #全てに等しく足す
    al = hand//N
    add(0,al)
    rem = hand%N
    add(B[i],-hand)
    add(B[i]+1,hand)
    if B[i]+rem<N:
        add(B[i]+1,1)
        add(B[i]+rem+1,-1)
    else:
        add(B[i]+1,1)
        add(0,1)
        add(B[i]+rem-N+1,-1)
ans = [getSum(i) for i in range(N)]
print(*ans)