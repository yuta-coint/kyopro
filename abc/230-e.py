n=  int(input())
ans = 0
for i in range(1,10**6+1):
    k = n//i
    ans+=max(0,k)
    ans+=max(0,k-10**6)
print(ans)