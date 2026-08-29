l = 0
r = 0
n,k = map(int,input().split())
window = [0 for i in range(k)]
a = list(map(lambda x:int(x)-1,input().split()))
ans = n+1
kind = 0
while l<n:
    if kind<k and r<n:
        if a[r]>=k:
            r+=1
            continue
        window[a[r]]+=1
        if window[a[r]]==1:
            kind+=1
        r+=1
    else:
        if kind==k:
            ans = min(ans,r-l)
        if a[l]>=k:
            l+=1
            continue
        window[a[l]]-=1
        if window[a[l]]==0:
            kind-=1
        l+=1
if ans == n+1:
    ans=0
print(ans)