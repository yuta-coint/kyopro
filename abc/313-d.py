N,K = map(int,input().split())
ans = []
for i in range(1,K+2):
    q = ["?"]
    for j in range(1,K+2):
        if i!=j:
            q.append(j)
    print(*q)
    T = int(input())
    ans.append(T)
if sum(ans[:K])%2!=ans[K]:
    for i in range(K+1):
        ans[i]=1-ans[i]
fore = sum(ans[:K-1])&1
for i in range(K+2,N+1):
    q = ["?"]+[j for j in range(1,K)]
    q.append(i)
    print(*q)
    T = int(input())
    ans.append(T^fore)
print(*(["!"]+ans))
