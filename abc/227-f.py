H,W,K = map(int,input().split())
K+=1
A = [list(map(int,input().split())) for i in range(H)]
#K+1番目が何で合計がいくつか
#i,jまで
dp = [float("inf") for i in range(H*W*K)]
#ijに到達するまでで大きい方k個の和を最小化したとき、k+1番目が何であるか
#dp[i][j][k-1]+A[i][j]が候補だが、A[i][j]>=dpb[i][j][k-1]で無ければ採択されない。この時dpb[i][j][k]=dpb[i-1][j][k-1]
#dp[i][j][k-1]+min(A[i][j],dpb[i][j][k-1])
#dp[i-1][j][k]をそのまま採択するにはA[i][j]>=dpb[i-1][j][k-1],この時dpb[i][j][k]=dpb[i-1][j][k-1]
#dp[i][j-1][k]をそのまま採択するにはA[i][j]>=dpb[i][j-1][k-1],この時dpb[i][j][k]=dpb[i][j-1][k-1]
dpb = [float("inf") for i in range(H*W*K)]
for i in range(H):
    for j in range(W):
        dp[i*W*K+j*K]=0
        if i==0 and j==0:
            dp[1]=A[0][0]
            continue
        for k in range(1,K):
            if j!=0:
                dp[i*W*K+j*K+k] = min(dp[i*W*K+(j-1)*K+k-1]+A[i][j],dp[i*W*K+(j-1)*K+k])
            if i!=0:
                dp[i*W*K+j*K+k] = min(dp[(i-1)*W*K+j*K+k-1]+A[i][j],dp[(i-1)*W*K+j*K+k])
            #else:
            #    dp[i*W*K+j*K+k] = min(dp[(i-1)*W*K+j*K+k-1]+A[i][j],dp[i*W*K+(j-1)*K+k-1]+A[i][j],dp[(i-1)*W*K+j*K+k],dp[i*W*K+(j-1)*K+k])
            