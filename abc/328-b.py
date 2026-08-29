N = int(input())
D = list(map(int,input().split()))
ans = 0
for mm in range(1,N+1):
    m = mm
    if m%11==0:
        m//=11
    if m>=10:
        continue
    for dd in range(1,D[mm-1]+1):
        d = dd
        if d%11==0:
            d//=11
        if d>=10:
            continue
        if m==d:
            ans+=1
print(ans)