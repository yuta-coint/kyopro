N,M = map(int,input().split())
A = list(map(int,input().split()))
#exceptionを除いて、Grundy数が小さい順に割り振られる
point_exc = {}
exc = []
cnt = 0
xys = [tuple(map(int,input().split())) for i in range(M)]
xys.sort()
for i in range(M):
    x,y= xys[i]
    if x in point_exc:
        exc[point_exc[x]].append(x-y)
    else:
        exc.append([x-y])
        point_exc[x]=cnt
        cnt+=1
for s in exc:
    s.sort()
Grundy_of_exception = {}
excepted = []
len_excepted = 0
def big_bisect(x):
    small = -1
    big = len_excepted
    while small+1<big:
        temp = (small+big)//2
        if excepted[temp]<x:
            small = temp
        else:
            big = temp
    return(big)
def Grundy(g):
    if g in Grundy_of_exception:
        return Grundy_of_exception[g]
    #除外すべきものの個数
    return g-big_bisect(g)
#複数かぶってたりして助かるやつ
residue = {}
def grundy_cal(x,y):
    excepted.append(x)
    global len_excepted
    len_excepted+=1
    Grundy_of_exception[x]=y
    if y in residue:
        residue[y]+=1
    else:
        residue[y]=1
for this_turn in point_exc:
    #print(this_turn,exc[point_exc[this_turn]])
    counting = {}
    grd_min = 10**20
    for next_turn in exc[point_exc[this_turn]]:
        #residueに入ってる以上の個数が入ってる奴らの中で一番小さいやつ
        grd =  Grundy(next_turn)
        if grd in residue:
            if grd in counting:
                counting[grd]+=1
            else:
                counting[grd]=1
            if counting[grd]>residue[grd]:
                if grd<grd_min:
                    grd_min = grd
        else:
            if grd<grd_min:
                grd_min = grd
    if grd_min<10**20:
        grundy_cal(this_turn,grd_min)
ans = 0
#print(Grundy_of_exception)
#print([Grundy(i) for i in range(100)])
for a in A:
    ans^=Grundy(a)
if ans==0:
    print("Aoki")
else:
    print("Takahashi")