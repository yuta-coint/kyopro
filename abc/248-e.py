N,K = map(int,input().split())
count = [0 for i in range(301)]
xpoint = []
ypoint = []
for i in range(N):
    x,y= map(int,input().split())
    xpoint.append(x)
    ypoint.append(y)
for i in range(N):
    a,b = xpoint[i],ypoint[i]
    for j in range(i+1,N):
        c,d = xpoint[j],ypoint[j]
        cnt=  0
        for k in range(N):
            x,y=xpoint[k],ypoint[k]
            if (d-b)*x-(c-a)*y==a*d-b*c:
                cnt+=1
        count[cnt]+=1
if K==1:
    print("Infinity")
else:
    ans = 0
    for i in range(K,301):
        ans+=count[i]//((i*(i-1))//2)
    print(ans)
