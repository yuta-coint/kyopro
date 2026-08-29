N = int(input())
listS = [(input(),i) for i in range(N)]
listS.sort()
lls = [len(listS[i][0]) for i in range(N)]
#前で確定のやつら
pre_l = [0]
pre = 1
for i in range(N-1):
    if lls[i]>lls[i+1]:
        pre=0
        pre_l.append(0)
        continue
    if listS[i]==listS[i+1][:lls[i]]:
        pre+=1
        if lls[i]==lls[i+1]:
            pre_l.append(pre_l[-1])
        else:
            pre_l.append(pre)
    else:
        pre=0
        pre_l.append(0)
#後ろで確定のやつら…番兵をおいてソートする
#trie木で検索する訓練もしなきゃなあ