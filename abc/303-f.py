ok = 10**18+1
ng = -1
N,H = map(int,input().split())
#tが同じものは適切に消していく
td = {}
tp = {}
LT = [0]
for i in range(N):
    t,d = map(int,input().split())
    if t in td:
        td[t]=max(d,td[t])
    else:
        td[t]=d
        LT.append(t)
    if t in tp:
        tp[t]=max(d*t,tp[t])   
    else:
        tp[t]=d*t
N = len(LT)-1
LT.sort()
#各区画ごとに最大の傾きと最大の火力を求める。
kata = []
power = []
for i in range(1,N+1):
    kata.append(td[LT[i]])
    power.append(tp[LT[i]])
k = [0]
mk = 0
for i in reversed(range(N)):
    if kata[i]>mk:
        mk = kata[i]
    k.append(mk)
k.reverse()
p = [0]
mp = 0
for i in range(N):
    if power[i]>mp:
        mp = power[i]
    p.append(mp)
LT.append(10**18+1)
#各エリアの総ダメージ計算
all_damage = []
cuts = []
print(LT,k,p)
for i in range(N+1):
    if k[i]*(LT[i+1]-1)<=p[i]:
        #横線が常に上
        all_damage.append(p[i]*(LT[i+1]-LT[i]))
        cuts.append(-1)
    elif k[i]*LT[i]>=p[i]:
        #斜線が常に上
        all_damage.append((LT[i+1]-LT[i])*(LT[i]+LT[i+1]-1)*k[i]//2)
        cuts.append(-2)
    else:
        #斜線が上になる最小値
        cut = (p[i]//k[i])+1
        cuts.append(cut)
        all_damage.append((cut-LT[i])*p[i]+(LT[i+1]-cut)*(cut+LT[i+1]-1)*k[i]//2)

while ng+1<ok:
    m=(ng+ok)//2
    #mターン使って勝てるか判定する
    damage = 0
    for i in range(N+1):
        if LT[i+1]>m:
            if cuts[i]==-1 or cuts[i]>m:
                damage+=p[i]*(m-LT[i])
            elif cuts[i]==-2:
                damage+=(m-LT[i])*(LT[i]+m-1)*k[i]//2
            else:
                damage+=((cuts[i]-LT[i])*p[i]+(m-cuts[i])*(cuts[i]+m-1)*k[i]//2)
            break
        else:
            #ターンを計算する
            damage+=all_damage[i]
    if damage>=H:
        ok = m
    else:
        ng = m
print(ok-1)