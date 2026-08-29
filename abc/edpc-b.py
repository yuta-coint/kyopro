N,K = map(int,input().split())
h = list(map(int,input().split()))
ans = [0]
if N<=K:
    print(abs(h[0]-h[N-1]))
    exit()
for i in range(1,K+1):
    ans.append(abs(h[0]-h[i]))
for i in range(K+1,N):
    ans.append(min([ans[i-width]+abs(h[i]-h[i-width]) for width in range(1,K+1)]))
print(ans[N-1])