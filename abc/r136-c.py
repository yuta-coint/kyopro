N = int(input())
a = list(map(int,input().split()))
ans = 0
ans += max(0,a[0]-a[N-1])
for i in range(N-1):
    ans+=max(0,a[i+1]-a[i])
ans = max(ans,max(a))
print(ans)