from time import perf_counter
from copy import deepcopy
start = perf_counter()
n,m = map(int,input().split())
initial = [[10**9]+list(map(int,input().split())) for i in range(m)]
#取り出せるだけ取り出す。移動を行うたびに実行しておけばいい。
def carry_out():
    global cnt
    for i in range(m):
        if capa[i]>0:
            if condition[i][-1]==cnt:
                ans.append((cnt,0))
                cnt+=1
                condition[i].pop()
                capa[i]-=1
                carry_out()
                return 0
    return 0
#下から確定させていく
def bottom_carry_out():
    global bottom_cnt
    for i in range(10):
        if capa[i]-bottom_ok[i]>0:
            if condition[i][bottom_ok[i]+1]==bottom_cnt:
                bottom_cnt-=1
                bottom_ok[i]+=1
                bottom_carry_out()
                return 0
    return 0
#箱vとその上にある全ての箱を別の山iに移す
from random import randint
def rand_without(ex):
    r = randint(0,8)
    if r>=ex:
        r+=1
    return r
def min_max():
    minL = [-1 for i in range(10)]
    for i in range(10):
        if capa[i]>bottom_ok[i]:
            minL[i] = min(condition[i])
    M = max(minL)
    return minL.index(M)
def move(v,i):
    global cost
    for j in range(m):
        if v in condition[j]:
            if i==j:
                break
            ans.append((v,i+1))
            cut = condition[j].index(v)
            moved_cnt = len(condition[j][cut:])
            cost += moved_cnt+1
            capa[i]+=moved_cnt
            capa[j]-=moved_cnt
            condition[i]+=condition[j][cut:]
            condition[j]=condition[j][:cut]
ans_last = []
score = 10**9
##########移動させる対象を上から見ていって、移動先の最小値よりも小さいものがあれば、その手前でカットする。
condition = deepcopy(initial)
cnt = 1
ans = []
cost = 0
capa = [20 for i in range(10)]
bottom_ok = [0 for i in range(10)]
bottom_cnt = 200
while cnt<=n:
    carry_out()
    bottom_carry_out()
    for j in range(m):
        if capa[j]==bottom_ok[j]:
            move(bottom_cnt,j)
            break
        if cnt in condition[j]:
            idousaki = min_max()
            hantei = min(condition[idousaki])
            for i in reversed(range(1,len(condition[j]))):
                if condition[j][i]==cnt:
                    if condition[j][i]==condition[j][-1]:
                        break
                    move(condition[j][i+1],idousaki)
                    break
                if condition[j][i]<hantei:
                    if condition[j][i]==condition[j][-1]:
                        continue
                    move(condition[j][i+1],idousaki)
                    idousaki = min_max()
                    hantei = min(condition[idousaki])
if cost<score:
    ans_last,score = deepcopy(ans),cost
########################################################
#でも無意味にでかくする意味はないから難しいところ################
for const in [140,150,160]:
    for key in range(40):
        for key2 in range(5,30):
            condition = deepcopy(initial)
            cnt = 1
            ans = []
            cost = 0
            capa = [20 for i in range(10)]
            bottom_ok = [0 for i in range(10)]
            bottom_cnt = 200
            while cnt<=n:
                carry_out()
                bottom_carry_out()
                for j in range(m):
                    if capa[j]==bottom_ok[j] and cnt<const:
                        idousaki = min_max()
                        for i in range(m):
                            if bottom_cnt in condition[i]:
                                fro = i
                                break
                        for i in reversed(range(1,len(condition[fro]))):
                            if condition[fro][i]==bottom_cnt:
                                break
                            if condition[fro][i]==condition[fro][-1]:
                                continue
                            if condition[fro][i]<cnt+key:
                                move(condition[fro][i+1],idousaki)
                                idousaki = min_max()
                        move(bottom_cnt,j)
                        break
                    if cnt in condition[j]:
                        idousaki = min_max()
                        hantei = min(condition[idousaki])
                        for i in reversed(range(1,len(condition[j]))):
                            if condition[j][i]==cnt:
                                if condition[j][i]==condition[j][-1]:
                                    break
                                if cnt>=const:
                                    for k in range(m):
                                        if capa[k]==bottom_ok[k]:
                                            idousaki = k
                                            break
                                move(condition[j][i+1],idousaki)
                                break
                            if condition[j][i]<hantei-key2+15:
                                if condition[j][i]==condition[j][-1]:
                                    continue
                                move(condition[j][i+1],idousaki)
                                idousaki = min_max()
                                hantei = min(condition[idousaki])
            if cost<score:
                ans_last,score = deepcopy(ans),cost
for s,t in ans_last:
    print(s,t)