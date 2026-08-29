n,x = map(int,input().split())
a = list(map(int,input().split()))
ans1 = x//a[n-1]
ans2 = ans1+1
x %= a[n-1]
for i in reversed(range(n-1)):
    x1 = x//a[i]
    x2 = x1+1
    kurai = a[i+1]//a[i]
    ans1,ans2 = min(ans1+x1,ans2+kurai-x1),min(ans1+x2,ans2+kurai-x2)
    x-=(x//a[i])*a[i]
print(ans1)