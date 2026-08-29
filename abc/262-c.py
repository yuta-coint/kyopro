N = int(input())
a = [0]+list(map(int,input().split()))
same = 0
ans = 0
for i in range(1,N+1):
    if a[i]==i:
        same+=1
    elif a[i]<i:
        if a[a[i]]==i:
            ans+=1
ans+=(same*(same-1))//2
print(ans)