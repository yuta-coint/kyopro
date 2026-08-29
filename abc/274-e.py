def main():
    import sys
    input = sys.stdin.readline
    N,M = map(int,input().split())
    v = N+M+1
    points = [(0,0)]+[tuple(map(int,input().split())) for i in range(N+M)]
    dist = [[0 for i in range(v)] for j in range(v)]
    for p in range(v):
        for q in range(v):
            dist[p][q]=((points[p][0]-points[q][0])**2+(points[p][1]-points[q][1])**2)**(1/2)
    ans = [[float("inf") for j in range(v)] for i in range(2**v)]
    box = [1 for i in range(2**v)]
    for i in range(2**v):
        for j in range(N+1,N+M+1):
            if (i>>j)&1:
                box[i]*=2
    #埋まり方がiで現在地がj
    ans[1][0]=0
    for i in range(2**v):
        for j in range(v):
            if (i>>j)&1:
                #直前にいた場所
                for k in range(v):
                    if j==k:
                        continue
                    if (i>>k)&1:
                        temp = ans[i-(1<<j)][k]+(dist[j][k]/box[i-(1<<j)])
                        if temp<ans[i][j]:
                            ans[i][j]=temp
    p = float('inf')
    for j in range(v):
        for b in range(1,2**M+1):
            if ans[b*(2**(N+1))-1][j]+(dist[j][0]/box[b*(2**(N+1))-1])<p:
                p=ans[b*(2**(N+1))-1][j]+(dist[j][0]/box[b*(2**(N+1))-1])
    print(p)
main()