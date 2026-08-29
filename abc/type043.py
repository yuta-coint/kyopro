from collections import deque
import sys
input = sys.stdin.readline
def main():
    H,W = map(int,input().split())
    rs,cs = map(lambda x:int(x)-1,input().split())
    rt,ct = map(lambda x:int(x)-1,input().split())
    INF  = 1<<60
    dist = [INF for _ in range(4*W*H)]
    for i in range(4):
        dist[i+cs*4+rs*4*W]=0
    chk = [False for _ in range(4*W*H)]
    hq = deque([(rs,cs,0),(rs,cs,1),(rs,cs,2),(rs,cs,3)])
    maze = [input() for i in range(H)]
    while hq:
        while hq:
            v = hq.pop()
            if chk[v[0]*4*W+v[1]*4+v[2]]:
                continue
            chk[v[0]*4*W+v[1]*4+v[2]]=True
            if v[2]==0:
                d = (0,-1)
            elif v[2]==1:
                d = (-1,0)
            elif v[2]==2:
                d = (0,1)
            else:
                d = (1,0)
            #壁にぶつかるか
            if v[0]+d[0]<0 or v[0]+d[0]>=H or v[1]+d[1]<0 or v[1]+d[1]>=W:
                continue
            #行く先に道はあるか
            if maze[v[0]+d[0]][v[1]+d[1]]=="#":
                continue
            for i in range(4):
                if v[2]==i:
                    if dist[d[0]*4*W+d[1]*4+i+v[0]*4*W+v[1]*4]>dist[v[0]*4*W+v[1]*4+v[2]]:
                        dist[d[0]*4*W+d[1]*4+i+v[0]*4*W+v[1]*4]=dist[v[0]*4*W+v[1]*4+v[2]]
                        hq.append((v[0]+d[0],v[1]+d[1],i))
                else:
                    if dist[d[0]*4*W+d[1]*4+i+v[0]*4*W+v[1]*4]>dist[v[0]*4*W+v[1]*4+v[2]]+1:
                        dist[d[0]*4*W+d[1]*4+i+v[0]*4*W+v[1]*4]=dist[v[0]*4*W+v[1]*4+v[2]]+1
                        if (v[2]+2)%2!=i:
                            hq.appendleft((v[0]+d[0],v[1]+d[1],i))
    #print(dist)
    print(min(dist[0+ct*4+rt*4*W],dist[1+ct*4+rt*4*W],dist[2+ct*4+rt*4*W],dist[3+ct*4+rt*4*W]))
main()