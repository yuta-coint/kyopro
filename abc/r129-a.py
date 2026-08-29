n,l,r = map(int,input().split())
b = len(bin(n))-2
ans = 0
for i in reversed(range(b)):
    if (n>>i)&1==0:
        continue
    mi = 2**i
    ma = 2**(i+1)
    if mi>r or ma<=l:
        continue
    else:
        ans+=min(r+1,ma)-max(l,mi)
print(ans)
