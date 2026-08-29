import sys
input = sys.stdin.readline
N = int(input())
pets = [list(map(int,input().split())) for i in range(N)]
M = int(input())
men = [list(map(int,input().split()))+[i] for i in range(M)]
phase = 0
part = [None for i in range(M)]
menl = sorted(men[:M//2])
menr = sorted(men[M//2:(M//2)*2])
lr = [0 for i in range(M)]
catch = [None for i in range(M)]
def move(i,j):
    a = ""
    d = j[0]-i[0]
    if d>0:
        a+="R"*d
    else:
        a+="L"*(-d)
    d = j[1]-i[1]
    if d>0:
        a+="D"*d
    else:
        a+="U"*(-d)
    return(a)
#置けますかチェック
def check(x,y):
    p = [[pet[i][0],pet[i][1]] for i in range(N)]
    pm = [[men[i][0],men[i][1]] for i in range(M)]
    cir = [[x,y],[max(x-1,1),y],[x,max(y-1,1)],[x,min(y+1,30)],[min(x+1,30),y]]
    for ci in cir:
        if ci in p:
            return(False)
    if ci[0] in pm:
        return(False)
    return(True)
first = move([men[0][0],men[0][1]],[1,15])
cnt = 2
for turn in range(300):
    ans = ["." for i in range(M)]
    if turn<len(first):
        ans[0]=first[turn]
    elif cnt<61 and cnt%2==0:
        if check[cnt//2][14]:
            ans[0]="u"
            cnt+=1
    elif cnt<61:
        ans[0]="R"
        cnt+=1
    print(*ans,sep="")
    sys.stdout.flush()
    #動物の動きをシュミレーションするぜ！
    m = list(input().split())
    for pet in range(N):
        for d in range(len(m[pet])):
            if m[pet][d]=="D":
                pets[pet][1]+=1
            elif m[pet][d]=="U":
                pets[pet][1]-=1
            elif m[pet][d]=="R":
                pets[pet][0]+=1
            elif m[pet][d]=="L":
                pets[pet][0]-=1