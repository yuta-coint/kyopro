#でかいやつから挿入していったら終わりそう。
pascal_size=  5001
mod = 998244353
pascal = [[0 for i in range(pascal_size)] for j in range(pascal_size)]
for i in range(pascal_size):
    for j in range(pascal_size):
        if i ==0 and j==0:
            pascal[0][0]=1
        if i>0:
            pascal[i][j]+=pascal[i-1][j]
        if j>0:
            pascal[i][j]+=pascal[i][j-1]
        pascal[i][j]%=mod
N,K = map(int,input().split())
A = list(map(int,input().split()))
score = [0 for i in range(K+1)]
cnt = [0 for i in range(N+1)]
for i in range(N):
    cnt[A[i]]+=1
perm = 0
pw = 1
for i in range(N+1):
    if cnt[i]==0:
        continue
    for t in range(1,cnt[i]+1):
        pw*=t
        pw%=mod
    if perm ==0:
        perm+=cnt[i]
        score[0]=1
        continue
    new_score = [0 for i in range(K+1)]
    #挿入する場所のうち、増えているところに挿入すると+0増えてないところに挿入すると+1
    #perm+1個の隙間のうち、増えるのがs+1個、増えないのがperm-s個
    #増えない隙間をdif個選ぶ→dif+s+1個の隙間の中から重複を許してcnt[i]-dif個選ぶ
    #増える隙間に何個入れるかを計算していかなきゃいけないのか
    for dif in range(cnt[i]+1):
        for s in range(K+1):
            if dif+s>K:
                break
            if perm-s-dif<0:
                continue
            new_score[s+dif]+=score[s]*pascal[perm-s-dif][dif]%mod*pascal[dif+s][cnt[i]-dif]%mod
            new_score[s+dif]%=mod
    perm += cnt[i]
    score = new_score
print(score[K]*pw%mod)