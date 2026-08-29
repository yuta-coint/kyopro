N,W = map(int,input().split())
ans = [0 for i in range(W+1)]
for _ in range(N):
    w,v = map(int,input().split())
    for j in reversed(range(w,W+1)):
        if ans[j]<ans[j-w]+v:
            ans[j]=ans[j-w]+v
print(max(ans))