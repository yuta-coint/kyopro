n,a,b=map(int,input().split())
v = list(map(int,input().split()))
v.sort(reverse=True)
cut_v = v[:a]
print(sum(cut_v)/a)
k1 = cut_v.count(v[a-1])
k2 = v.count(v[a-1])
if v[0]!=v[a-1]:
    ans = 1
    for i in range(k1):
        ans*=k2-i
        ans//=i+1
    print(ans)
else:
    ans = 0
    for j in range(a,b+1):
        if j>k2:
            break
        temp=1
        for i in range(k1+j-a):
            temp*=k2-i
            temp//=i+1
        ans+=temp
    print(ans)