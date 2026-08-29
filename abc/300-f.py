N,M,K = map(int,input().split())
S = list(input())
cx = S.count("x")
if cx*M<=K:
    print(N*M)
    exit()
loop = K//cx
ans = loop*N
K%=cx
#とりあえずM=1に帰着できた。
#[l:r)の中のxの数がK個以下になるように最大値を探す
r = 0
cnt = 0
ans_p = 0
if loop<M-1:
    S = S+S
    N *= 2
for l in range(N):
    while cnt<=K and r<N:
        #print(cnt,r)
        if r-l>ans_p:
            ans_p = r-l
        if S[r]=="x":
            cnt+=1
        r+=1
    if r==N and cnt<=K and ans_p<r-l:
        ans_p = r-l   
    if S[l]=="x":
        cnt-=1
print(ans+ans_p)