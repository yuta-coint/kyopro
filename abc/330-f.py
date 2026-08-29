ok = 10**9
ng = -1
N,K = map(int,input().split())
X=[]
Y=[]
for i in range(N):
    x,y  = map(int,input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
from bisect import bisect_left,bisect_right
sum_X = [0]
sum_Y= [0]
for i in range(N):
    sum_X.append(sum_X[-1]+X[i])
    sum_Y.append(sum_Y[-1]+Y[i])
while ng+1<ok:
    m = (ng+ok)//2
    l,r = 0,X[-1]+1
    while l+1<r:
        temp = (l+r)//2
        s1 = bisect_left(X,temp)
        s3 = bisect_left(X,temp+m)
        if s1>N-s3:
            r = temp
        else:
            l = temp
    left = l
    bl = bisect_right(X,left+m)
    br = bisect_right(X,left)
    lhands = sum_X[-1]-sum_X[bl]-(N-bl)*(left+m)+br*left-sum_X[br]


    l,r = 0,Y[-1]+1
    while l+1<r:
        temp = (l+r)//2
        s1 = bisect_left(Y,temp)
        s3 = bisect_left(Y,temp+m)
        if s1>N-s3:
            r = temp
        else:
            l = temp
    left = l
    bl = bisect_right(Y,left+m)
    br = bisect_right(Y,left)
    rhands = sum_Y[-1]-sum_Y[bl]-(N-bl)*(left+m)+br*left-sum_Y[br]
    #print(m,lhands,rhands)
    if lhands+rhands<=K:
        ok = m
    else:
        ng = m
print(ok)