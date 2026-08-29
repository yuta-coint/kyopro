T = int(input())
for case in range(T):
    S = list(input())
    B=S.count("B")
    A=len(S)-B
    #Aを何個使えるかという視点。
    term2 = []
    cnt = 0
    for i in range(len(S)):
        if S[i]=="B":
            term2.append(cnt)
            cnt = 0
        else:
            cnt+=1
    term2.append(cnt)
    pres = []
    cost = []
    temp = 0
    for i in range(len(term2)):
        if term2[i]&1:
            cost.append(temp)
            temp = 0
            pres.append(term2[i]//2)
        else:
            temp+=(term2[i]//2)-1
    cost.append(temp)
    if cost[0]==-1:
        cost[0]=0
    if cost[-1]==-1:
        cost[-1]=0
    #あとは何組ペアを消せるかを考えればよい
    #A-残ったpresの個数が消費できるAの上限であるので、Bの値と見比べて答えを出す。
    