N,M  = map(int,input().split())
if N*N<M:
    print(-1)
    exit()
ans = 10**24
for a in range(1,10**6+1):
    if a>N:
        break
    b = ((M-1)//a)+1
    if b>N:
        continue
    if a*b<ans:
        ans = a*b
print(ans)