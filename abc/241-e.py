n,k = map(int,input().split())
a = list(map(int,input().split()))
visited = [False for i in range(n)]
ans = 0
cnt = 0
point = [0 for i in range(n)]
la = [0 for i in range(n)]
b = [0]
while True:
    cnt+=1
    if visited[ans%n]:
        loop = cnt-point[ans%n]
        oneloop = ans+a[ans%n]-b[point[ans%n]]
        b.append(ans+a[ans%n])
        break
    visited[ans%n] = True
    point[ans%n]=cnt
    la[ans%n]=ans
    ans+=a[ans%n]
    #print(ans)
    b.append(ans)
#print(oneloop)
#print(loop)
if cnt>k:
    print(b[k])
else:
    ans = b[cnt]
    k-=cnt
    ans += oneloop*(k//loop)
    ans += b[(k%loop)+cnt-loop]-b[cnt-loop]
    print(ans)
