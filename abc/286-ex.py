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
from math import sqrt
def dist(point1,point2):
    return(sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2))
N = int(input())
poly = [tuple(map(int,input().split())) for i in range(N)]
s = tuple(map(int,input().split()))
t = tuple(map(int,input().split()))
points_s = convex_hull([s,t]+poly,N+2)
#両方凸包に入っていたら直結、そうじゃなければ外周を回る
if s in points_s and t in points_s:
    p1 = points_s.index(s)
    p2 = points_s.index(t)
    if p1>p2:
        p1,p2=p2,p1
    p3 = len(points_s)+p1
    points_s = points_s+points_s
    ans1 = 0
    for i in range(p1,p2):
        ans1+=dist(points_s[i],points_s[i+1])
    ans2 = 0
    for i in range(p2,p3):
        ans2+=dist(points_s[i],points_s[i+1])
    print(min(ans1,ans2))
else:
    print(dist(s,t))