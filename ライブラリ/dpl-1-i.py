def SME_with_side(K,L,a):
    from collections import deque
    window = deque([])
    r = (a[0],0)
    ans = []
    for i in range(K):
        f = 0
        if window:
            r=window.pop()
            f = 1
        while r[0]>a[i] and window:
            r=window.pop()
        if (r[0]<=a[i] or i==0) and f==1:
            window.append(r)
        window.append((a[i],i))
        if i<L-1:
            ans.append(window[0][0])
            continue
        ans.append(window[0][0])
        if window[0][1]<=i+1-L:
            window.popleft()
    return(ans)
N,W = map(int,input().split())
Max_vi = 0
products=[]
for i in range(N):
    v,w,m = map(int,input().split())
    Max_vi = max(Max_vi,v)
    products.append((v,w,m))
dp = [float('inf') for i in range(N*Max_vi*Max_vi+1)]
dp[0]=0
for _ in range(N):
    v,w,m = products[0],products[1],products[2]
    #rem…を価値をvで割ったあまり
    for rem in range(v):
        #価値x*v+remの奴らについて重さを考える
        table = []
        x=0
        while x*w+rem<=N*Max_vi*Max_vi:
            table.append(dp[x*w+rem]-x*w)
            x+=1
        #print(table)
        temp = SME_with_side(x,m+1,table)
        #print(temp)
        for i in range(x):
            dp[i*w+rem]=temp[i]+i*w
    #print(dp)

