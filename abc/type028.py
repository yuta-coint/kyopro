import sys
input = sys.stdin.readline
n = int(input())
paper_edge = [[0 for j in range(1001)] for i in range(1001)]
for i in range(n):
    lx,ly,rx,ry= map(int,input().split())
    paper_edge[lx][ly]+=1
    paper_edge[lx][ry]-=1
    paper_edge[rx][ly]-=1
    paper_edge[rx][ry]+=1
ans = [0 for i in range(n+1)]
paper_c = [0 for i in range(1001)]
for i in range(1001):
    for j in range(1001):
        paper_c[j]+=paper_edge[i][j]
    paper = [0 for i in range(1002)]
    for j in range(1,1002):
        paper[j] = paper[j-1]+paper_c[j-1]
    for j in range(1001):
        ans[paper[j]]+=1
for i in range(1,n+1):
    print(ans[i])