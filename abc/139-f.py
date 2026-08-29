#y/xが小さい順にソートします
#2つのリストにそれぞれ分母と分子を並べる
import array
from math import sqrt
##(0,0)を入れるとバグる
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
xvector = []
yvector = []
for i in range(N):
    x,y = map(int,input().split())
    if x==0 and y==0:
        N-=1
        continue
    xvector.append(x)
    yvector.append(y)
if N==0:
    N=1
    xvector.append(0)
    yvector.append(0)
sorted_vector = arg_sort(xvector,yvector)
l = 0
r = 1
#これ全探索で良かったりする？長さ100でスタート地点100で個数100やし
sorted_vector = [list(sorted_vector[0]),list(sorted_vector[1])]
temp = [(sorted_vector[0][i],sorted_vector[1][i]) for i in range(N)]
#print(temp)
ans = 0
#print(sorted_vector)
for start in range(N):
    for  length in range(1,N+1):
        tempx = 0
        tempy = 0
        for i in range(start,start+length):
            tempx+=sorted_vector[0][i%N]
            tempy+=sorted_vector[1][i%N]
        #print(tempx,tempy)
        if ans<tempx**2+tempy**2:
            ans = tempx**2+tempy**2
print(sqrt(ans))