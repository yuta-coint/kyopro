import time
start = time.perf_counter()
import random as rd
from heapq import heapify,heappop,heappush
N, L = map(int,input().split())
T= list(map(int,input().split()))
def calc(G):
    cnt = [0 for i in range(N)]
    now = 0
    for _ in range(1000):
        cnt[now]+=1
        now = G[now][cnt[now]%2]
    for i in range(N):
      cnt[i]*=500
    score = 0
    sabun = []
    for i in range(N):
        score+=abs(T[i]-cnt[i])
        sabun.append(-T[i]+cnt[i])
    return score,sabun,cnt
final = [((i+1)%N,(i+2)%N) for i in range(N)]
ideal = 10**14
TT = [(-T[i],i) for i in range(N)]
heapify(TT)
tuika = []
for i in range(N):
    p,q = heappop(TT)
    tuika.append(q)
    heappush(TT,(p+2500,q))
for sana in range(70):
    ans = [((i+sana+1)%N,tuika[(i-sana)%N]) for i in range(N)]
    for _ in range(1000):
        #仕事しすぎている人を辞めさせる。
        sc,sab,cnt = calc(ans)
        if sc<ideal:
            final = ans
            ideal = sc
        hataraki = rd.randint(0,N-1)
        sabori = rd.randint(0,N-1)
        cut = rd.randint(0,N-1)
        jun = [i for i in range(cut,N)]+[i for i in range(cut)]
        for i in jun:
            if sab[i]<sab[sabori]:
                if rd.randint(0,99)<95:
                    sabori = i
            if sab[i]>sab[hataraki]:
                if rd.randint(0,99)<95:
                    hataraki = i
        temp = (0,0,ans[0][0])
        flag = 0
        cut = rd.randint(0,N-1)
        jun = [i for i in range(cut,N)]+[i for i in range(cut)]
        for i in jun:
            for j in range(2):
                if ans[i][j]==hataraki:
                    if j==0:
                        ans[i] = (sabori,ans[i][1])
                    else:
                        ans[i] = (ans[i][0],sabori)
                    temp = (i,j,sabori)
                    flag = 1
                    break
            if flag == 1:
                break
        #print(sc)
ans = final
sc,sab,cnt = calc(ans)
#print(sc)
while time.perf_counter()-start <1.9:
    if sc<ideal:
        final = ans
        ideal = sc
    hataraki = rd.randint(0,N-1)
    sabori = rd.randint(0,N-1)
    cut = rd.randint(0,N-1)
    jun = [i for i in range(cut,N)]+[i for i in range(cut)]
    for i in jun:
        if sab[i]<sab[sabori]:
            if rd.randint(0,99)<95:
                sabori = i
        if sab[i]>sab[hataraki]:
            if rd.randint(0,99)<95:
                hataraki = i
    hataraki2 = rd.randint(0,N-1)
    sabori2 = rd.randint(0,N-1)
    while hataraki2==hataraki:
        hataraki2 = rd.randint(0,N-1)
    while sabori2 == sabori:
        sabori2 = rd.randint(0,N-1)
    cut = rd.randint(0,N-1)
    jun = [i for i in range(cut,N)]+[i for i in range(cut)]
    for i in jun:
        if hataraki == i or sabori==i:
            continue
        if sab[i]<sab[sabori2]:
            if rd.randint(0,99)<95:
                sabori2 = i
        if sab[i]>sab[hataraki2]:
            if rd.randint(0,99)<95:
                hataraki2 = i
    temp = (0,0,ans[0][0])
    flag = 0
    cut = rd.randint(0,N-1)
    jun = [i for i in range(cut,N)]+[i for i in range(cut)]
    for i in jun:
        for j in range(2):
            if ans[i][j]==hataraki:
                temp = (i,j,ans[i][j])
                if j==0:
                    ans[i] = (sabori,ans[i][1])
                else:
                    ans[i] = (ans[i][0],sabori)
                flag = 1
                break
        if flag == 1:
            break
    flag = 0
    for i in jun:
        for j in range(2):
            if ans[i][j]==hataraki2:
                temp2 = (i,j,ans[i][j])
                if j==0:
                    ans[i] = (sabori2,ans[i][1])
                else:
                    ans[i] = (ans[i][0],sabori2)
                flag = 1
                break
        if flag == 1:
            break
    new_sc,new_sab,new_cnt = calc(ans)
    if sc>new_sc ^ rd.randint(0,99)>=90:
        sc,sab,cnt = new_sc,new_sab,new_cnt
    else:
        i,j,old = temp2
        if j== 0:
            ans[i] = (old,ans[i][1])
        else:
            ans[i] = (ans[i][0],old)
        i,j,old = temp
        if j== 0:
            ans[i] = (old,ans[i][1])
        else:
            ans[i] = (ans[i][0],old)
    
    #print(sc)
for i in range(N):
    print(*final[i])