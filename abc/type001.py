n,L = map(int,input().split())
k = int(input())
a = list(map(int,input().split()))
a = [0]+a+[L]
m = 1
M = L
while m+1<M:
    ans = (m+M)//2
    cnt = 0
    yokan = 0
    for i in range(n+1):
        if a[i+1]-a[i]+yokan>=ans:
            cnt+=1
            yokan = 0
        else:
            yokan+=a[i+1]-a[i]
    #print(cnt)
    if cnt<k+1:
        M = ans
    else:
        m = ans
print(m)
