window = {}
l = 0
r = 0
n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
kind = 0
while l<n:
    if kind<=k and r<n:
        ans = max(ans,r-l)
        if a[r] in window:
            window[a[r]]+=1
        else:
            window[a[r]]=1
        if window[a[r]]==1:
            kind+=1
        r+=1
    else:
        if kind<=k:
            ans = max(ans,r-l)
        window[a[l]]-=1
        if window[a[l]]==0:
            kind-=1
        l+=1
if kind<=k:
    ans = max(ans,r-l)
print(ans)