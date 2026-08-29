#ボブは黒マスに移動させたら勝ち
#アリスは白で囲まれているマスに移動させ続けなればならない。
T = int(input())
for _ in range(T):
    N = int(input())
    A = [list(map(int,input().split())) for i in range(N)]
    B = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if j > 0:
                B[i][j] += A[i][j-1]
            if j < N - 1:
                B[i][j] += A[i][j+1]
    front_dp = [[B[i][j] for j in range(N)] for i in range(N)]
    for i in range(1,N):
        for j in range(N):
            temp = 10**24
            if j > 0:
                temp = front_dp[i-1][j-1]
            if j < N-1:
                if temp > front_dp[i-1][j+1]:
                    temp = front_dp[i-1][j+1]
            front_dp[i][j] += temp
    back_dp = [[B[i][j] for j in range(N)] for i in range(N)]
    for i in reversed(range(N-1)):
        for j in range(N):
            temp = 10**24
            if j > 0:
                temp = back_dp[i+1][j-1]
            if j < N-1:
                if temp > back_dp[i+1][j+1]:
                    temp = back_dp[i+1][j+1]
            back_dp[i][j] += temp
    ans = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            ans[i][j] = back_dp[i][j]
            if i == 0:
                continue
            temp = 10**24
            if j > 0:
                temp = front_dp[i-1][j-1]
            if j < N-1:
                if temp > front_dp[i-1][j+1]:
                    temp = front_dp[i-1][j+1]
            ans[i][j] += temp
    #for i in range(N):
     #   print(back_dp[i])
    real_ans = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            temp = 10**24
            if j > 0:
                temp = ans[i][j-1]
            if j < N - 1:
                if temp > ans[i][j+1]:
                    temp = ans[i][j+1]
            real_ans[i][j] = temp
    for i in range(N):
        print(*real_ans[i])