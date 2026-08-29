def main():
    import sys
    input = sys.stdin.readline
    N,M = map(int,input().split())
    S = [input() for i in range(N)]
    s=[[0 for i in range(2*M)]+[(1 if S[i][j]=="O" else 0) for j in range(N)] for i in range(N)]
    #右上に向かって全部足し合わせたやつ
    dp1 = [[0 for i in range(2*M+N)] for j in range(N)]
    for i in range(N):
        dp1[i][2*M+N-1]=s[i][2*M+N-1]
        dp1[i][2*M+N-2]=s[i][2*M+N-2]
        dp1[0][2*M+i]=s[0][2*M+i]
    for i in range(1,N):
        for j in reversed(range(2*M+N-2)):
            dp1[i][j] = dp1[i-1][j+2]+s[i][j]
    #右上の三角形に向かって全部足し合わせる
    dp2 = [[0 for i in range(2*M+N+1)] for j in range(N)]
    for i in range(N):
        for j in reversed(range(2*M+N)):
            dp2[i][j]=dp2[i][j+1]+dp1[i][j]
    #四角形の累積和
    square = [[0 for i in range(N+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(N):
            square[i+1][j+1]=square[i][j+1]+square[i+1][j]-square[i][j]+s[i][j+2*M]
    #print(dp1)
    #print(dp2)
    #print(square)
    Q = int(input())
    for i in range(Q):
        x,y = map(lambda x:int(x)-1,input().split())
        ans = dp2[x][y+1]-(dp2[x-M][y+2*M+1] if x-M>=0 else 0)
        #print(ans)
        if x-M>=0:
            ans-=square[x+1][N]-square[x+1][y+1]-square[x+1-M][N]+square[x+1-M][y+1]
            #print("B")
        else:
            ans-=square[x+1][N]-square[x+1][y+1]
            #print("A")
        print(ans)
main()