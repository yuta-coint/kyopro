import sys
input = sys.stdin.readline
def main():
    N = int(input())
    points = []
    power = []
    for i in range(N):
        x,y,P = map(int,input().split())
        points.append((x,y))
        power.append(P)
    dist = [[0 for i in range(N)] for j in range(N)]
    ok = [[0 for i in range(N)] for j in range(N)]
    chk = []
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            dist[i][j]=(abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])-1)//power[i]
            chk.append((dist[i][j]+1,i,j))
    chk.sort()
    m = 0
    M = len(chk)
    while m+1<M:
        temp = (m+M)//2
        G = [[] for i in range(N)]
        for i in range(temp):
            G[chk[i][1]].append(chk[i][2])
        ok = False
        for s in range(N):
            visited = [False for i in range(N)]
            S = [s]
            visited[s]=True
            while S!=[]:
                v = S.pop()
                for i in G[v]:
                    if visited[i]==False:
                        visited[i]=True
                        S.append(i)
            for i in range(N):
                if visited[i]==False:
                    break
            else:
                ok=True
        if ok:
            M=temp
        else:
            m=temp
    #print(M)
    print(chk[M-1][0])
main()


