import sys
input = sys.stdin.readline
N,W = map(int,input().split())
oti = [[] for i in range(W)]
for i in range(N):
    X,Y = map(int,input().split())
    oti[X-1].append((Y-1,i))
kieru_time = [-1 for i in range(N)]
kaisu = 10**9
for i in range(W):
    oti[i].sort()
    if kaisu>len(oti[i]):
        kaisu = len(oti[i])
for i in range(kaisu):
    time = 0
    for j in range(W):
        if oti[j][i][0]>time:
            time = oti[j][i][0]
    for j in range(W):
        kieru_time[oti[j][i][1]]=time
#print(kieru_time)
Q = int(input())
for case in range(Q):
    T,A = map(int,input().split())
    if kieru_time[A-1]==-1 or kieru_time[A-1]>T-1:
        print("Yes")
    else:
        print("No")