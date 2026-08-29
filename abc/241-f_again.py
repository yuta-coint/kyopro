H,W,N = map(int,input().split())
sx,sy = map(int,input().split())
gx,gy = map(int,input().split())
from bisect import bisect
#r行目の様子をみる
dr = {}
wallr = [[0,W+1] for i in range(N)]
dc = {}
#c列目の様子をみる
wallc = [[0,H+1] for i in range(N)]
cnt1 = 0
cnt2 = 0
for i in range(N):
    r,c = map(int,input().split())
    if not (r in dr):
        dr[r]=cnt1
        cnt1+=1
    wallr[dr[r]].append(c)
    if not (c in dc):
        dc[c]=cnt2
        cnt2+=1
    wallc[dc[c]].append(r)
for i in range(N):
    wallc[i].sort()
    wallr[i].sort()
def U_instruction(rs,cs,l):
    if cs in dc:
        #print(wallc[dc[cs]])
        lim = wallc[dc[cs]][bisect(wallc[dc[cs]],rs)-1]
        #print(lim)
    else:
        lim = 0
    if lim==0:
        return(-1)
    else:
        return((max(rs-l,lim+1)),cs)
def D_instruction(rs,cs,l):
    if cs in dc:
        lim = wallc[dc[cs]][bisect(wallc[dc[cs]],rs)]
    else:
        lim = H+1
    if lim==H+1:
        return(-1)
    else:
        return((min(rs+l,lim-1),cs))
def L_instruction(rs,cs,l):
    if rs in dr:
        lim = wallr[dr[rs]][bisect(wallr[dr[rs]],cs)-1]
    else:
        lim=0
    if lim==0:
        return(-1)
    else:
        return((rs,max(cs-l,lim+1)))
def R_instruction(rs,cs,l):
    if rs in dr:
        lim = wallr[dr[rs]][bisect(wallr[dr[rs]],cs)]
    else:
        lim=W+1
    if lim==W+1:
        return(-1)
    else:
        return((rs,min(cs+l,lim-1)))
import queue
big = 10**9+10
visited = set()
S = queue.Queue()
visited.add(sx*big+sy)
S.put((sx*big+sy,0))
ans = -1
while not S.empty():
    v = S.get()
    if v[0]==gx*big+gy:
        ans = v[1]
        break
    x = v[0]//big
    y = v[0]%big
    neighbor = [L_instruction(x,y,float('inf')),R_instruction(x,y,float('inf')),U_instruction(x,y,float('inf')),D_instruction(x,y,float('inf'))]
   # print(neighbor)
    for link in neighbor:
        if link==-1:
            continue
        i=link[0]*big+link[1]
        if not (i in visited):
            visited.add(i)
            #print(i//big,i%big,v[1]+1)
            S.put((i,v[1]+1))
print(ans)