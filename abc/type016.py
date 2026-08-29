n = int(input())
a,b,c = map(int,input().split())
ans = float('inf')
for i in range(10**4):
    for j in range(10**4):
        if n-a*i-b*j>=0 and (n-a*i-b*j)%c==0:
            ans = min(ans,(n-a*i-b*j)//c)
print(ans)