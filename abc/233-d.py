n,k = map(int,input().split())
a = list(map(int,input().split()))
for i in range(1,n):
    a[i]+=a[i-1]
count={0:1}
ans = 0
for i in range(n):
    if a[i]-k in count:
        ans+=count[a[i]-k]
    if a[i] in count:
        count[a[i]]+=1
    else:
        count[a[i]]=1   
print(ans)