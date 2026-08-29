def main():
    import sys
    input = sys.stdin.readline
    H,W = map(int,input().split())
    R = list(map(int,input().split()))
    C = list(map(int,input().split()))
    A = [list(input()) for i in range(H)]
    dp = [0 for i in range(4*H*W)]
    dp[1] = C[0]
    dp[2] = R[0]
    dp[3] = C[0]+R[0]
    for j in range(1,W):
        for b in range(4):
            if A[0][j]==A[0][j-1]:
                dp[j*4+b] = dp[(j-1)*4+b]
            else:
                dp[j*4+b] = dp[(j-1)*4+(b^1)]
            if b&1:
                dp[j*4+b]+=C[j]
    for i in range(1,H):
        for j in range(W):
            for b in range(4):
                if A[i][j]==A[i-1][j]:
                    dp[i*4*W+j*4+b] = dp[(i-1)*4*W+j*4+b]+(R[i] if (b>>1)&1 else 0)
                else:
                    dp[i*4*W+j*4+b] = dp[(i-1)*4*W+j*4+(b^2)]+(R[i] if (b>>1)&1 else 0)
                if j>0:
                    if A[i][j]==A[i][j-1]:
                        ta = dp[i*4*W+(j-1)*4+b]+(C[j] if b&1 else 0)
                        if ta < dp[i*4*W+j*4+b]:
                            dp[i*4*W+j*4+b] = ta
                    else:
                        ta = dp[i*4*W+(j-1)*4+(b^1)]+(C[j] if b&1 else 0)
                        if ta < dp[i*4*W+j*4+b]:
                            dp[i*4*W+j*4+b] = ta
    #print(dp)
    print(min(dp[4*H*W-4:]))
main()