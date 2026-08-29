N,K=map(int,input().split())
a = list(map(int,input().split()))
mi = float('inf')
for i in reversed(range(K)):
    if mi>a[i]:
        mi = a[i]
    else:
        a[i]=-1
cnt =K
ans = float("inf")
for i in range(K):
    if a[i]==-1:
        continue
    while True:
        if cnt==N:
            break
        if a[cnt]>a[i]:
            ans = min(ans,cnt-i)
            break
        else:
            cnt+=1
if ans == float('inf'):
    print(-1)
else:
    print(ans)
    

