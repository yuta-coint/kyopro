n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
t = 0
for i in range(n):
    t+=abs(a[i]-b[i])
if k>=t and (k-t)%2 == 0:
    print("Yes")
else:
    print("No")