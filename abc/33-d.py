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
ans =0
def arg_sort(a,b):
    area1,area2,area3 = [[],[]],[[],[]],[[],[]]
    N = len(a)
    for i in range(N):
        if a[i]>0 and b[i]>=0:
            area1[0].append(a[i])
            area1[1].append(b[i])
        elif a[i]<=0 and b[i]>=0:
            area2[0].append(a[i])
            area2[1].append(b[i])
        else:
            area3[0].append(a[i])
            area3[1].append(b[i])
    sorted = []
    p,q = frac_sort(area1[0],area1[1])
    sorted=[p,q]
    p,q = frac_sort(area2[0],area2[1])
    sorted[0]+=p
    sorted[1]+=q
    p,q = frac_sort(area3[0],area3[1])
    sorted[0]+=p
    sorted[1]+=q
    return(sorted)
N = int(input())
points = [list(map(int,input().split())) for _ in range(N)]
parp = 0
obtu = 0
for i in range(N):
    xvector =[]
    yvector =[]
    for j in range(N):
        if i==j:
            continue
        xvector.append(points[j][0]-points[i][0])
        yvector.append(points[j][1]-points[i][1])
    sorted_vector = arg_sort(xvector,yvector)
    #print(sorted_vector)
    xvector,yvector = sorted_vector[0],sorted_vector[1]
    L = len(xvector)
    l = 0
    r = 1
    r2 = 1
    while l<L:
        #r2を180度より大きくする→rを90度調整より大きくする→間を数える
        if xvector[l]*yvector[r2]>xvector[r2]*yvector[l] and l!=r2:
            r2+=1
            r2%=L
        elif xvector[l]*xvector[r]+yvector[l]*yvector[r]>0 and xvector[l]*yvector[r]>xvector[r]*yvector[l] and l!=r:
            r+=1
            r%=L
        elif xvector[l]*xvector[r]+yvector[l]*yvector[r]==0 and xvector[l]*yvector[r]>xvector[r]*yvector[l] and l!=r:
            parp += 1
            r+=1
            r%=L
        else:
            #print(r2,r)
            obtu+=(r2-r)%L
            #print(obtu)
            if l==r2:
                r2-=1
                r2%=L
            if l==r:
                r-=1
                r%=L
            l+=1
            if l==r2:
                r2+=1
                r2%=L
            if l==r:
                r+=1
                r%=L
acut = (N*(N-1)*(N-2))//6-obtu-parp
print(acut,parp,obtu)