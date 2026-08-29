import sys
input=sys.stdin.readline
h,w,n=map(int,input().split())
ans=[0 for i in range(10)]
ans[0] = (h-2)*(w-2)
point = set()
for i in range(n):
    a,b = map(lambda x:int(x)-1,input().split())
    point.add((a,b))
    for h1 in (-1,0,1):
        for w1 in (-1,0,1):
            if a+h1<=0 or a+h1>=h-1 or b+w1<=0 or b+w1>=w-1:
                continue
            cnt = 0
            for h2 in (-1,0,1):
                for w2 in (-1,0,1):
                    if (a+h1+h2,b+w1+w2) in point:
                        cnt+=1
            ans[cnt-1]-=1
            ans[cnt]+=1
    #print(ans)
for i in range(10):
    print(ans[i])

