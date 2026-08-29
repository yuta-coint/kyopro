n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = float("inf")
for i in range(n):
    ans = min(a[i]*b[i],ans)
ans = min(max(a)*min(b),ans)
print(ans)