n,l,w = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = 0
for i in range(n-1):
    if a[i]+w<a[i+1]:
        ans+=(a[i+1]-w-a[i]-1)//w
        ans+=1
if a[0]>0:
    ans+=(a[0]-1)//w
    ans+=1
if a[n-1]<l-w:
    ans+=(l-w-a[n-1]-1)//w
    ans+=1
print(ans)

