def main():
    from collections import deque
    def SME(K,L,a):
        window = deque([])
        r = (a[0],0)
        ans = []
        for i in range(K):
            f = 0
            if window:
                r=window.pop()
                f = 1
            while r[0]>a[i] and window:
                r=window.pop()
            if (r[0]<=a[i] or i==0) and f==1:
                window.append(r)
            window.append((a[i],i))
            if i<L-1:
                continue
            l = window.popleft()
            ans.append(l[0])
            if l[1]>i+1-L:
                window.appendleft(l)
        return(ans)
    import sys
    input = sys.stdin.readline
    H0,W0,h1,w1,h2,w2 = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(H0)]
    if w1<w2:
        w2 = w1
    if h1<h2:
        h2 = h1
    a_sum = [[0 for j in range(W0+1)] for i in range(H0+1)]
    for i in range(H0):
        for j in range(W0):
            a_sum[i+1][j+1] = a[i][j] - a_sum[i][j] + a_sum[i+1][j] + a_sum[i][j+1]
    black_stamp = [[0 for j in range(W0-w1+1)] for i in range(H0-h1+1)]
    white_stamp = [[0 for j in range(W0-w2+1)] for i in range(H0-h2+1)]
    for i in range(H0-h1+1):    
        for j in range(W0-w1+1):
            black_stamp[i][j] = a_sum[i+h1][j+w1] - a_sum[i][j+w1] - a_sum[i+h1][j] + a_sum[i][j]
    for i in range(H0-h2+1):
        for j in range(W0-w2+1):
            white_stamp[i][j] -= a_sum[i+h2][j+w2] - a_sum[i][j+w2] - a_sum[i+h2][j] + a_sum[i][j]
    #H,W,L　H×Lのリストの中からL*Dの最小値を求める
    #H,W,L,Dはそれぞれの箱の大きさ
    #各区画でWhite_stampの最小値を求める
    White_min_row = []
    for i in range(H0-h2+1):
        White_min_row.append(SME(W0-w2+1,w1-w2+1,white_stamp[i]))
    white_min = []
    for j in range(W0-w1+1):
        t = [White_min_row[i][j] for i in range(H0-h2+1)]
        white_min.append(SME(H0-h2+1,h1-h2+1,t))
    #print(black_stamp)
    #print(white_stamp)
    #print(White_min_row)
    #print(white_min)
    ans = 0
    for i in range(H0-h1+1):
        for j in range(W0-w1+1):
            ans = max(black_stamp[i][j]+white_min[j][i],ans)
    print(ans)
main()