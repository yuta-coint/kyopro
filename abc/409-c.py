N,L = map(int,input().split())
d = list(map(int,input().split()))
D = {i:0 for i in range(L)}
cnt = 0
D[0]+=1
for i in range(N-1):
    cnt += d[i]
    cnt %= L
    D[cnt] += 1
if L%3 != 0:
    print(0)
    exit()
ans = 0
M = L//3
for a in D:
    if a<M:
        ans += D[a]*D[a+M]*D[a+M+M]
print(ans)