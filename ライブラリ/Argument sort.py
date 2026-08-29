#y/xが小さい順にソートします
#2つのリストにそれぞれ分母と分子を並べる
import array
def frac_sort(a,b):
    N = len(a)
    point0 = array.array('i',[])
    point1 = array.array('i',[])
    for i in range(N):
        x,y = a[i],b[i]
        if i==0:
            point0.append(x)
            point1.append(y)
            continue
        ma = i
        mi = -1
        while ma>mi+1:
            m = (ma+mi)//2
            if y*point0[m]>=x*point1[m]:
                mi = m
            else:
                ma = m
        point0.insert(mi+1,x)
        point1.insert(mi+1,y)
    return(point0,point1)
def arg_sort(a,b):
    Quadrant = [[[],[]] for i in range(4)]
    N = len(a)
    for i in range(N):
        if a[i]>0 and b[i]>=0:
            Quadrant[0][0].append(a[i])
            Quadrant[0][1].append(b[i])
        elif a[i]<=0 and b[i]>0:
            Quadrant[1][0].append(-a[i])
            Quadrant[1][1].append(b[i])
        elif a[i]<0 and b[i]<=0:
            Quadrant[2][0].append(-a[i])
            Quadrant[2][1].append(-b[i])
        else:
            Quadrant[3][0].append(a[i])
            Quadrant[3][1].append(-b[i])
    sorted = []
    p,q = frac_sort(Quadrant[0][0],Quadrant[0][1])
    sorted.append([p,q])
    q,p = frac_sort(Quadrant[1][1],Quadrant[1][0])
    q = map(lambda x: x*(-1),q)
    sorted.append([p,q])
    p,q = frac_sort(Quadrant[2][0],Quadrant[2][1])
    q = map(lambda x: x*(-1),q)
    p = map(lambda x: x*(-1),p)
    sorted.append([p,q])
    q,p = frac_sort(Quadrant[3][1],Quadrant[3][0])
    p = map(lambda x: x*(-1),p)
    sorted.append([p,q])
    return(sorted)


