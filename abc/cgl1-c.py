import sys
input = sys.stdin.readline
x0,y0,x1,y1 = map(int,input().split())
q = int(input())
for i in range(q):
    x,y = map(int,input().split())
    if (y1-y0)*(x-x0)>(x1-x0)*(y-y0):
        print("CLOCKWISE")
    elif (y1-y0)*(x-x0)<(x1-x0)*(y-y0):
        print("COUNTER_CLOCKWISE")
    elif (x1-x0)*(x-x0)<0 or (y1-y0)*(y-y0)<0:
        print("ONLINE_BACK")
    elif (x0-x1)*(x-x1)<0 or (y0-y1)*(y-y1)<0:
        print("ONLINE_FRONT")
    else:
        print("ON_SEGMENT")
def clockwise(x0,y0,x1,y1,x2,y2):
    if (y1-y0)*(x2-x0)>(x1-x0)*(y2-y0):
        print(True)
    elif (y1-y0)*(x2-x0)<(x1-x0)*(y2-y0):
        return(False)
    elif (x1-x0)*(x2-x0)<0 or (y1-y0)*(y2-y0)<0:
        print("ONLINE_BACK")
    elif (x0-x1)*(x2-x1)<0 or (y0-y1)*(y2-y1)<0:
        print("ONLINE_FRONT")
    else:
        print("ON_SEGMENT")
