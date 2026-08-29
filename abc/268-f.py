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

N = int(input())
ans = 0
c = []
n = []
for i in range(N):
    S = input()
    cnt = 0
    num = 0
    for j in range(len(S)):
        if S[j]=="X":
            cnt+=1
        else:
            ans += int(S[j])*cnt
            num += int(S[j])
    c.append(cnt)
    n.append(num)
cc,nn = frac_sort(c,n)
snn = []
snn.append(sum(nn))
for i in range(N):
    snn.append(snn[-1]-nn[i])
for i in range(N):
    ans+=cc[i]*snn[i+1]
print(ans)