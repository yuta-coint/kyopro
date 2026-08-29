#平方分割！！！
mod = 998244353
pascal = [[0 for i in range(1000)] for j in range(1000)]
for i in range(1000):
    for j in range(1000):
        if i ==0 and j==0:
            pascal[0][0]=1
        if i>0:
            pascal[i][j]+=pascal[i-1][j]
        if j>0:
            pascal[i][j]+=pascal[i][j-1]
        pascal[i][j]%=mod
N = int(input())
a = [list(map(int,input().split())) for i in range(N)]
cnt = [[] for i in range(N**2+1)]
for i in range(N):
    for j in range(N):
        cnt[a[i][j]].append(i*N+j)
ans = 0
for label in range(N*N+1):
    cnt_label = len(cnt[label])
    if cnt_label>=N:
        pat = [0 for i in range(N*N)]
        for p in cnt[label]:
            pat[p]+=1
        for ij in range(N*N):
            if ij//N>0:
                pat[ij]+=pat[ij-N]
            if ij%N>0:
                pat[ij]+=pat[ij-1]
            pat[ij]%=mod
        for p in cnt[label]:
            ans+=pat[p]
            ans%=mod
    else:
        for x in range(cnt_label):
            for y in range(x,cnt_label):
                di = cnt[label][y]%N-cnt[label][x]%N
                dj = cnt[label][y]//N-cnt[label][x]//N
                if di>=0 and dj>=0:
                    ans+=pascal[di][dj]
                    ans%=mod
print(ans)