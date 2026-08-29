import sys
input = sys.stdin.readline
#2点のベクトルを求める
def vec(a, b):
    return (a[0] - b[0], a[1] - b[1])
N = int(input())
poly = [tuple(map(int,input().split())) for i in range(N)]
mi = 10**16
ma = -10**16
for i in range(N):
    if poly[i][0]<mi:
        cut = i
        mi = poly[i][0]
    if poly[i][0]>ma:
        cut2=i
        ma = poly[i][0]
vert_left=-1
vert_right = -1
poly = poly+poly
if cut<cut2:
    poly_down = poly[cut:cut2+1]
else:
    poly_down = poly[cut:cut2+N+1]
if cut>cut2:
    poly_up = poly[cut2:cut+1]
else:
    poly_up = poly[cut2:cut+N+1]
upper_check = []
downer_check = []
upper_boarder = []
downer_boarder = []
upper_edge = []
downer_edge =[]
ld = len(poly_down)
lu = len(poly_up)
for i in range(len(poly_down)-1):
    x,y = vec(poly_down[i+1],poly_down[i])
    downer_check.append((-y,x))
    downer_boarder.append(-y*poly_down[i][0]+x*poly_down[i][1])
    downer_edge.append(poly_down[i][0])
    if x==0:
        s,t = poly_down[i][1],poly_down[i+1][1]
        if s>t:
            s,t = t,s
        if poly_down[i][0]==ma:
            vert_right = (s,t)
        else:
            vert_left = (s,t)
for i in range(len(poly_up)-1):
    x,y = vec(poly_up[i+1],poly_up[i])
    upper_check.append((-y,x))
    upper_boarder.append(-y*poly_up[i][0]+x*poly_up[i][1])
    upper_edge.append(poly_up[i][0])
    if x==0:
        s,t = poly_up[i][1],poly_up[i+1][1]
        if s>t:
            s,t = t,s
        if poly_up[i][0]==ma:
            vert_right = (s,t)
        else:
            vert_left = (s,t)
Q = int(input())
for _ in range(Q):
    a,b = map(int,input().split())
    if a>ma or a<mi:
        print("OUT")
        continue
    IN = True
    ON = True
    ok = ld-1
    ng = 0
    while ng+1<ok:
        temp = (ok+ng)//2
        if downer_edge[temp]<a:
            ng = temp
        else:
            ok = temp
    if a*downer_check[ng][0]+b*downer_check[ng][1]<downer_boarder[ng]:
        IN,ON=False,False
    elif a*downer_check[ng][0]+b*downer_check[ng][1]==downer_boarder[ng]:
        IN = False
    ok = lu-1
    ng = 0
    while ng+1<ok:
        temp = (ok+ng)//2
        if upper_edge[temp]>a:
            ng = temp
        else:
            ok = temp
    if a*upper_check[ng][0]+b*upper_check[ng][1]<upper_boarder[ng]:
        IN,ON=False,False
    elif a*upper_check[ng][0]+b*upper_check[ng][1]==upper_boarder[ng]:
        IN = False
    if a==ma:
        IN = False
        if vert_right!=-1:
            if vert_right[0]>b or vert_right[1]<b:
                ON=False
    if a==mi:
        IN = False
        if vert_left!=-1:
            if vert_left[0]>b or vert_left[1]<b:
                ON=False
    if IN:
        print("IN")
    elif ON:
        print("ON")
    else:
        print("OUT")