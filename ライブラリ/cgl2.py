def para_ortho(x_p0,y_p0,x_p1,y_p1,x_p2,y_p2,x_p3,y_p3):
    if (x_p1-x_p0)*(y_p3-y_p2)==(y_p1-y_p0)*(x_p3-x_p2):
        print(2)
    elif (x_p1-x_p0)*(x_p3-x_p2)+(y_p1-y_p0)*(y_p3-y_p2)==0:
        print(1)
    else:
        print(0)
def intersection(x0,y0,x1,y1,x2,y2,x3,y3):
    if (-y1*x2+y0*x2+x1*y2-x0*y2-x1*y0+x0*y1)*(-y1*x3+y0*x3+x1*y3-x0*y3-x1*y0+x0*y1)<=0:
        return(1)
    else:
        return(0)
q = int(input())
for i in range(q):
    x_p0,y_p0,x_p1,y_p1,x_p2,y_p2,x_p3,y_p3 = map(int,input().split())
    print(intersection(x_p0,y_p0,x_p1,y_p1,x_p2,y_p2,x_p3,y_p3)&intersection(x_p2,y_p2,x_p3,y_p3,x_p0,y_p0,x_p1,y_p1))