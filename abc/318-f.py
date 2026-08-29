#二つの区間の集合共通部分をとる各区間は[a,b)で表される
def section_isc(sec1,sec2):
    inout = []
    for x,y in sec1:
        inout.append((x,1))
        inout.append((y,-1))
    for x,y in sec2:
        inout.append((x,1))
        inout.append((y,-1))
    inout.sort()
    cnt = 1
    ret = []
    for i in range(1,len(inout)):
        if cnt==2:
            ret.append((inout[i-1][0],inout[i][0]))
        cnt+=inout[i][1]
    return(section_reo(ret))
INF = 10**19
#区間の集まりを全部disjointにする。
def section_reo(sec):
    sec.sort()
    l = -INF
    r= -INF
    ret = []
    for p,q in sec:
        if r>=p:
            if l!=-INF:
                if q>=r:
                    l,r = l,q
            else:
                l,r = p,q
        else:
            if l<r:
                ret.append((l,r))
            l,r = p,q
    if l<r:
        ret.append((l,r))
    return ret

N= int(input())
X = list(map(int,input().split()))
L = list(map(int,input().split()))
ans = [(-10**19,10**19)]
for i in range(N):
    newsec = []
    for j in range(N-i):
        mi = X[i+j]-L[i]
        ma = X[j]+L[i]+1
        if mi>=ma:
            continue
        newsec.append((mi,ma))
    newsec = section_reo(newsec)
    print(newsec)
    ans = section_isc(ans,newsec)
pr = 0
for l,r in ans:
    pr+=r-l
print(pr)
