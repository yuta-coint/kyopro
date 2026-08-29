n = int(input())
a = list(map(int,input().split()))
ans = [0,0]
for i in range(n-1):
    ans.append(ans[i+1]*2-ans[i]+a[i+1])
if ans[n]%n!=0:
    print(-1)
else:
    for i in range(n):
        ans[i]-=i*ans[n]//n
    if ans[1]+ans[n-1]-ans[0]*2!=a[0]:
        print(-1)
    else:
        ans=ans[:n]
        print(sum(ans)-min(ans)*n)