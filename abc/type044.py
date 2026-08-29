N,Q = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0
for i in range(Q):
    t,x,y = map(lambda x:int(x)-1,input().split())
    if t==0:
        a[(x-cnt)%N],a[(y-cnt)%N]=a[(y-cnt)%N],a[(x-cnt)%N]
    elif t==1:
        cnt+=1
    else:
        print(a[(x-cnt)%N])
    #print(a)
