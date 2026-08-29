N = int(input())
cnt = [0]
for n in range(1,N):
    temp=0
    a = 1
    while a*a<n:
        if n%a==0:
            temp+=1
        a+=1
    temp*=2
    if a*a==n:
        temp+=1
    cnt.append(temp)
ans = 0
for i in range(1,N):
    ans+=cnt[i]*cnt[N-i]
print(ans)