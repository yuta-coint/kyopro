N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.append(-1)
b.append(-1)
pr = set()
prb = set()
lan = [0]
ran = [0]
cnt = 0
tp = 0
tpb = 0
for i in range(N):
    if a[i] in pr:
        lan.append(lan[-1])
        ran.append(ran[-1])
        continue
    pr.add(a[i])
    tp+=1
    #包含できる限り増やし続けて種類数が一致しているか検証
    while b[cnt] in pr and cnt<N:
        if b[cnt] not in prb:
            prb.add(b[cnt])
            tpb+=1
        if tpb==tp:
            lan.append(cnt)
            break
        cnt+=1
    else:
        lan.append(-1)
        ran.append(-1)
    if lan[-1]==-1:
        continue
    while b[cnt] in pr and cnt<N:
        cnt+=1
    ran.append(cnt)
Q = int(input())
for i in range(Q):
    s,t = map(int,input().split())
    if lan[s]<t and ran[s]>=t:
        print("Yes")
    else:
        print("No")




