import sys
sys.setrecursionlimit(300000)
def dfs(v):
    global mother
    global lowlink
    global check
    global counter
    global cnt
    global ord
    if v == 0:
        cnt = 0
    ord[v]=counter
    lowlink[v]=ord[v]
    counter+=1
    check[v]=1
    for i in G[v]:
        if check[i]==0:
            mother[i] = v
            dfs(i)
            lowlink[v] = min(lowlink[v],lowlink[i])
            if v == 0:
                 cnt += 1
        elif i != mother[v]:
            lowlink[v] = min(lowlink[v],ord[i])

#mother = [None for i in range(81)]
#lowlink = [None for i in range(81)]
#check=[0 for i in range(81)]
counter = 0
cnt = 0
#橋じゃないものと4以外を全部列挙する
def is_not_art(N):
    global mother
    global lowlink
    global check
    global counter
    global ord
    ord = [None for i in range(N)]
    mother = [None for i in range(N)]
    lowlink = [None for i in range(N)]
    check=[0 for i in range(N)]
    counter = 0
    cnt = 0
    art = []
    dfs(0)
    #print(ord)
    #print(lowlink)
    #print(mother)
    #for i in range(E):G_pair[i].sort()
    #G_pair.sort()
    for i in range(N):
        if i==0 or (i+4)%81 in blocked:
            continue
        if ord[mother[i]]<=lowlink[i] and mother[i]!=0:
            art.append(mother[i])
    if cnt >1:
        art.append(0)
    articulation = set(art)
    r = []
    for i in range(N):
        if i==0 or (i+4)%81 in blocked:
            continue
        if not (i in articulation):
            r.append((i+4)%81)
    return r

D,blocks = map(int,input().split())

block_and_container = blocks
blocked = set()
for i in range(blocks):
    ri,rj = map(int,input().split())
    blocked.add(ri*D+rj)
#とりあえず入れた逆の順で運び出すことができれば正の得点を得られるはず。
dtc = {}
for i in range(81):
    dtc[i] = (i//9)*2+abs(i%9-4)
    if i%9==0 or i%9==8:
        dtc[i]+=15
    if i//9==9:
        dtc[i]+=15
    if (i-1 in blocked or i+1 in blocked) and (i-9 in blocked or i+9 in blocked):
        dtc[i]+=30
dtc2 = {}
for i in range(81):
    dtc2[i] = (i//9)*2+abs(i%9-4)
    if i//9+i%9<=1 or i//9-i%9<=-7 or i%9+i//9>=15 or i//9-i%9>=7:
        dtc2[i]-=10
dtc3 = {}
for i in range(81):
    dtc3[i] = (i//9)*2+abs(i%9-4)
    if i//9+i%9<=1 or i//9-i%9<=-7 or i%9+i//9>=15 or i//9-i%9>=7 or i//9==8 or i%9==0 or i%9==8:
        dtc3[i]-=10
insert_order = []
cntn = [-1 for i in range(D*D)]
for _ in range(D*D-1-blocks):
    G = [[] for i in range(D*D)]
    for i in range(D-1):
        for j in range(D):
            s = i*D+j
            t = (i+1)*D+j
            if s in blocked or t in blocked:
                continue
            G[(s-4)%81].append((t-4)%81)
            G[(t-4)%81].append((s-4)%81)
    for i in range(D):
        for j in range(D-1):
            s = i*D+j
            t = i*D+j+1
            if s in blocked or t in blocked:
                continue
            G[(s-4)%81].append((t-4)%81)
            G[(t-4)%81].append((s-4)%81)
    for i in range(D*D):
        G[i].sort()
    td = int(input())
    cand = is_not_art(81)
    pt = cand[0]
    for c in cand:
        if td<20:
            if dtc[c]<dtc[pt]:
                pt = c
        elif td>60-blocks:
            if dtc[c]>dtc[pt]:
                pt = c
        elif td<40:
            if dtc3[c]>dtc3[pt]:
                pt=c
        else:
            if dtc2[c]>dtc2[pt]:
                pt = c
    if td<20:
        if pt%9!=0:
            if dtc[pt-1]>0:
                dtc[pt-1]-=100
            else:
                dtc[pt-1]+=15
        if pt%9!=8:
            if dtc[pt+1]>0:
                dtc[pt+1]-=100
            else:
                dtc[pt+1]+=15
        if pt//9!=0:
            if dtc[pt-9]>0:
                dtc[pt-9]-=100
            else:
                dtc[pt-9]+=15
        if pt//9!=8:
            if dtc[pt+9]>0:
                dtc[pt+9]-=100
            else:
                dtc[pt+9]+=15
    print(pt//D,pt%D)
    cntn[pt] = td
    insert_order.append(pt)
    block_and_container+=1
    blocked.add(pt)
#運び出す順序をとりあえず貪欲にすれば多少はましになるはず
from heapq import heapify,heappop,heappush
ejectable = [(cntn[3],3),(cntn[5],5),(cntn[13],13)]
heapify(ejectable)
unejected = [True for i in range(D*D)]
unejected[4]=False
unejected[3]=False
unejected[5]=False
unejected[13]=False
for i in reversed(range(D*D-1-blocks)):
    cl,pl =heappop(ejectable)
    print(pl//D,pl%D)
    if pl%9!=0:
        if cntn[pl-1]!=-1 and unejected[pl-1]:
            heappush(ejectable,(cntn[pl-1],pl-1))
            unejected[pl-1]=False
    if pl%9!=8:
        if cntn[pl+1]!=-1 and unejected[pl+1]:
            heappush(ejectable,(cntn[pl+1],pl+1))
            unejected[pl+1]=False
    if pl//9!=8:
        if cntn[pl+9]!=-1 and unejected[pl+9]:
            heappush(ejectable,(cntn[pl+9],pl+9))
            unejected[pl+9]=False
    if pl//9!=0:
        if cntn[pl-9]!=-1 and unejected[pl-9]:
            heappush(ejectable,(cntn[pl-9],pl-9))
            unejected[pl-9]=False