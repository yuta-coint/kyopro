NN,K,P = map(int,input().split())
#一番左がAの左がx,右がyで不一致なのがk箇所のものを求める
ans = [[[1]]]
for N in range(2,NN+1):
    ans_sum = [[[0 for y in range(N)] for x in range(N)] for k in range(N)]
    #各kについて累積和を求める
    for k in range(N-1):
        for x in range(1,N):
            for y in range(1,N):
                ans_sum[k][x][y]=(ans[k][x-1][y-1]+ans_sum[k][x-1][y]+ans_sum[k][x][y-1]-ans_sum[k][x-1][y-1])%P
    ans = [[[0 for y in range(N)] for x in range(N)] for k in range(N)]
    for k in range(N):
        for x in range(N):
            for y in range(N):
                if k==0:
                    ans[k][x][y]=(-ans_sum[k][x][y]*2+ans_sum[k][x][N-1]+ans_sum[k][N-1][y])%P
                    continue
                ans[k][x][y]=(ans_sum[k-1][x][y]*2+ans_sum[k-1][N-1][N-1]-ans_sum[k-1][N-1][y]-ans_sum[k-1][x][N-1]-ans_sum[k][x][y]*2+ans_sum[k][x][N-1]+ans_sum[k][N-1][y])%P
                ans[k][x][y]%=P
p=0
for i in range(NN):
    p+=sum(ans[K][i])%P
    p%=P
print(p)