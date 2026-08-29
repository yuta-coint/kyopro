#https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D
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
#https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/1/DPL_1_G
N,W = map(int,input().split())
dp = [0 for i in range(W+1)]
for _ in range(N):
    v,w,m = map(int,input().split())
    #rem…重さをwで割ったあまり
    for rem in range(w):
        #おもさx*w+remの奴らについて重さを考える
        table = []
        x=0
        while x*w+rem<=W:
            table.append(-dp[x*w+rem]+x*v)
            x+=1
        #print(table)
        temp = SME_with_side(x,m+1,table)
        #print(temp)
        for i in range(x):
            dp[i*w+rem]=-temp[i]+i*v
    #print(dp)
print(dp[W])


