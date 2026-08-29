def clockwise(x0,y0,x1,y1,x2,y2):
    if (y1-y0)*(x2-x0)>(x1-x0)*(y2-y0):
        return(True)
    elif (y1-y0)*(x2-x0)<(x1-x0)*(y2-y0):
        return(False)
    elif (x1-x0)*(x2-x0)<0 or (y1-y0)*(y2-y0)<0:
        return(False)
    elif (x0-x1)*(x2-x1)<0 or (y0-y1)*(y2-y1)<0:
        return(True)
    else:
        return(False)
def counter_clockwise(x0,y0,x1,y1,x2,y2):
    if (y1-y0)*(x2-x0)>(x1-x0)*(y2-y0):
        return(False)
    elif (y1-y0)*(x2-x0)<(x1-x0)*(y2-y0):
        return(True)
    elif (x1-x0)*(x2-x0)<0 or (y1-y0)*(y2-y0)<0:
        return(False)
    elif (x0-x1)*(x2-x1)<0 or (y0-y1)*(y2-y1)<0:
        return(True)
    else:
        return(False)
def convex_hull(points,N):
    points.sort()
    points.sort(key=lambda val: val[1])
    #print(points)
    ans = []
    convex_hull_upper = [points[0],points[1]]
    ls = 2
    for i in range(2,N):
        while ls>1:
            if clockwise(convex_hull_upper[ls-2][0],convex_hull_upper[ls-2][1],convex_hull_upper[ls-1][0],convex_hull_upper[ls-1][1],points[i][0],points[i][1]):
                break
            convex_hull_upper.pop()
            ls-=1
        convex_hull_upper.append(points[i])
        ls+=1
    convex_hull_downer = [points[0],points[1]]
    ld = 2
    for i in range(2,N):
        while ld>1:
            if counter_clockwise(convex_hull_downer[ld-2][0],convex_hull_downer[ld-2][1],convex_hull_downer[ld-1][0],convex_hull_downer[ld-1][1],points[i][0],points[i][1]):
                break
            convex_hull_downer.pop()
            ld-=1
        convex_hull_downer.append(points[i])
        ld+=1
        #print(convex_hull_downer)
    convex_hull_upper.reverse()
    return(convex_hull_downer+convex_hull_upper[1:ls-1])
def area(polygon,N):
    #2倍になっている
    ans = 0
    for i in range(1,N-1):
        ans+=(polygon[i][0]-polygon[0][0])*(polygon[i+1][1]-polygon[0][1])-(polygon[i][1]-polygon[0][1])*(polygon[i+1][0]-polygon[0][0])
    return(ans)
N = int(input())
points = [tuple(map(int,input().split())) for i in range(N)]
convex_hull_AtCfarm = convex_hull(points,N)
lch = len(convex_hull_AtCfarm)
ans = area(convex_hull_AtCfarm,lch)-N*2+2
#あとは外周を調べるだけ
convex_hull_AtCfarm.append(convex_hull_AtCfarm[0])
from math import gcd
edge = 0
for i in range(lch):
    edge+=gcd(convex_hull_AtCfarm[i][0]-convex_hull_AtCfarm[i+1][0],convex_hull_AtCfarm[i][1]-convex_hull_AtCfarm[i+1][1])
ans+=edge
print(ans//2)