N = int(input())
ans = float('inf')
for a in range(10**6+1):
    m = -1
    M = 10**6+1
    while m+1<M:
        b = (m+M)//2
        x = (a**2+b**2)*(a+b)
        if x>=N:
            M = b
        else:
            m=b
    ans = min(ans,(a**2+M**2)*(a+M))
print(ans)
