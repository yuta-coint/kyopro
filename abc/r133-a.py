n = int(input())
a = list(map(int,input().split()))
t = a[n-1]
for i in range(n-1):
    if a[i]>a[i+1]:
        t = a[i]
        break
ans = []
for i in range(n):
    if a[i]!=t:
        ans.append(a[i])
print(*ans)