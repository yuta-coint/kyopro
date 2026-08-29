N = int(input())
pets = [list(map(int,input().split())) for i in range(N)]
M = int(input())
men = [list(map(int,input().split()))+[i] for i in range(M)]
phase = 0
part = [None for i in range(M)]
menl = sorted(men[:M//2])
menr = sorted(men[M//2:(M//2)*2])
menl.sort()
menr.sort()
lr = [0 for i in range(M)]
catch = [None for i in range(M)]
for i in range(M//2):
    part[menl[3]]=[1,6*i+1]
    part[menr[3]]=[3,6*i+5]
    catch[menl[3]]=[2,6*i+3]
    catch[menr[3]]=[2,6*i+3]
    lr[menr[3]]=1
zero = ["" for i in range(M)]
for i in range(M):
    d = part[i][0]-men[i][0]
    if d>0:
        zero[i]+="R"*d
    else:
        zero[i]+="L"*(-d)
    d = part[i][1]-men[i][1]
    if d>0:
        zero[i]+="U"*d
    else:
        zero[i]+="D"*(-d)
L = [len(zero(i)) for i in range(M)]
mL=max(L)
firstl = "rURrURrUU"
firstr = "lDLlDLlDD"
stock = [-1 for i in range(M)]
stock2 = [[] for i in range(M)]
moved = "DRRRRRRU"
moveu = "URRRRRRD"
for turn in range(300):
    attack = 0
    #動物攻撃確認
    for point in catch:
        if point in pets:
            if point[]
    if turn==mL:
        phase = 1
    if turn==mL+9:
        phase = 2
    ans = ""
    if phase==0:
        for man in range(M):
            if L[man]<=turn:
                ans+="."
            else:
                ans+=zero[turn]
    elif phase==1:
        for man in range(M):
            if lr[man]==1:
                ans+=firstr[turn-mL]
            else:
                ans+=firstl[turn-mL]
    else:
        for man in range(M):
            if stock[man]==-1:
                #通常業務
                if attack==1:
                    if lr[man]==0:
                        ans+="d"
                        stock[man]=16
                        stock2[man]=moveu+firstr
                    else:
                        ans+="u"
                        stock[man]=16
                        stock2[man]=moved+firstl
                else:
                    ans+="."
            else:
                ans+=stock2[man][stock[man]]
                stock[man]-=1
    print(ans)
    #動物の動きをシュミレーションするぜ！
    for pet in range(N):
        m = list(input())
        for dir in m:
            if dir=="D":
                pets[pet][1]-=1
            elif dir=="U":
                pets[pet][1]+=1
            elif dir=="R":
                pets[pet][0]+=1
            elif dir=="L":
                pets[pet][0]-=1