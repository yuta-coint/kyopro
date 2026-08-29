x = int(input())
l = len(str(x))
candidate = []
for sa in range(10):
    for m in range(1,10):
        c = m
        d = m
        for i in range(l-1):
            d+=sa
            if d<0 or d>9:
                break
            c*=10
            c+=d
        else:
            candidate.append(c)
for sa in range(10):
    for m in range(1,10):
        c = m
        d = m
        for i in range(l-1):
            d-=sa
            if d<0 or d>9:
                break
            c*=10
            c+=d
        else:
            candidate.append(c)
candidate.append(10)
m = 0
for i in range(18):
    m*=10
    m+=1
    candidate.append(m)
ans = 10**18+1
for can in candidate:
    if can>=x:
        ans = min(ans,can)
print(ans)
    
