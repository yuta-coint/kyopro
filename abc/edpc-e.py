N,W = map(int,input().split())
ans = [10**16 for value in range(10**5+1)]
ans[0]=0
for i in range(N):
    w,v = map(int,input().split())
    for value in reversed(range(v,10**5+1)):
        if ans[value]>ans[value-v]+w:
            ans[value]=ans[value-v]+w
for i in reversed(range(10**5+1)):
    if ans[i]<=W:
        print(i)
        break
