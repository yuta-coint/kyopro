N = int(input())
d = {}
A = list(map(int,input().split()))
ans = 0
for i in A:
    if i in d:
        if d[i]==0:
            d[i]=1
        else:
            d[i]=0
            ans+=1
    else:
        d[i]=1
print(ans)
