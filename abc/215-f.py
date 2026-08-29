N = int(input())
points = [tuple(map(int,input().split())) for _ in range(N)]
points.sort()
minl = [float('inf') for i in range(N)]
minr = [float('inf') for i in range(N)]
maxl = [0 for i in range(N)]
maxr = [0 for i in range(N)]
minl[0]=points[0][1]
maxl[0]=points[0][1]
minr[0]=points[N-1][1]
maxr[0]=points[N-1][1]
for i in range(1,N):
    minl[i]=min(minl[i-1],points[i][1])
    maxl[i]=max(minl[i-1],points[i][1])
for i in reversed(range(N-1)):
    minl[i]=min(minl[i+1],points[i][1])
    maxl[i]=max(minl[i+1],points[i][1])
ok = 0
ng = 10**7
#二分探索sliding window
while ok+1<ng:
    temp = (ok+ng)>>1
    r = 1
    for l in range(N):
        ##狭すぎたらr+=1として、十分あれば値を記録して次のループへ
        while r<N:
            if 
            r+=1
