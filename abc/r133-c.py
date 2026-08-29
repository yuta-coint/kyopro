h,w,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = (k-1)*(h-1)*(w-1)
rc = 0
for i in range(h-1):
    rc+=(a[i]-(k-1)*(w-1))%k
rr = 0
for i in range(w-1):
    rr+=(b[i]-(k-1)*(h-1))%k
if (a[h-1]-rr)%k == (b[w-1]-rc)%k:
    ans+=rc
    ans+=rr
    if (h-1)*(k-1)-rc>(w-1)*(k-1)-rr:
        ans += (w-1)*(k-1)-rr
        ans += (a[h-1]-(w-1)*(k-1))%k
    else:
        ans += (h-1)*(k-1)-rc
        ans += (b[w-1]-(h-1)*(k-1))%k
else:
    ans = -1
print(ans)


