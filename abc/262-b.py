import sys
input = sys.stdin.readline
def main():
    N,M = map(int,input().split())
    G = [[False for i in range(N)] for j in range(N)]
    for i in range(M):
        u,v = map(lambda x:int(x)-1,input().split())
        G[u][v]=True
        G[v][u]=True
    ans=0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if G[i][j] and G[j][k] and G[k][i]:
                    ans+=1
    print(ans)
main()