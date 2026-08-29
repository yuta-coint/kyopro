N,W,K,C = map(int,input().split())
Water = [tuple(map(int,input().split())) for i in range(W)]
House = [tuple(map(int,input().split())) for i in range(K)]
#S = [list(map(int,input().split())) for i in range(N)]
score = 0
"""def test(x,y,p):
    global score
    score+=p+C
    if S[x][y]<=p:
        S[x][y]=0
        return(1)
    else:
        S[x][y]-=p
        return(0)"""

def nearest_water(x,y):
    r = -1
    mhd = 50000
    for i in range(W):
        if abs(Water[i][0]-x)+abs(Water[i][1]-y)<mhd:
            mhd = abs(Water[i][0]-x)+abs(Water[i][1]-y)
            r = Water[i]
    return(r)
def nearest_water2(x,y):
    r = -1
    mhd = 50000
    for i in range(N):
        for j in range(N):
            if enemy[i][j]:
                if abs(i-x)+abs(j-y)<mhd:
                    mhd = abs(i-x)+abs(j-y)
                    r = (i,j)
    return(r)
#横断
def across(x1,y1,x2,y2):
    if y1<y2:
        y1toy2 = range(y1,y2)
    else:
        y1toy2 = reversed(range(y2+1,y1+1))
    for j in y1toy2:
        if enemy[x1][j]:
            return()
        enemy[x1][j]=True
    if x1<x2:
        x1tox2 = range(x1,x2+1)
    else:
        x1tox2 = reversed(range(x2,x1+1))
    for i in x1tox2:
        if enemy[i][y2]:
            return()
        enemy[i][y2]=True


#壊すべきセルを特定する。
enemy = [[False for j in range(N)] for i in range(N)]
for i,j in Water:
    enemy[i][j]=True
for k in range(K):
    xg,yg = nearest_water2(House[k][0],House[k][1])
    across(House[k][0],House[k][1],xg,yg)
import sys
ssf = sys.stdout.flush
#適当に壊す
parameter = {1:30,2:60,4:90,8:120,16:160,32:190,64:240,128:372}
for i in range(N):
    for j in range(N):
        if enemy[i][j]:
            while True:
                print(i,j,372)
                ssf()
                #a = test(i,j,372)
                a = int(input())
                if a==2:
                    exit()
                if a==1:
                    break
print(score)