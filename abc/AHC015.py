import sys
f = list(map(int,input().split()))
sys.setrecursionlimit(10**6)
#箱の中のスコアを計算する
def caluculate(box):
    tree = [i for i in range(100)]
    size = [1 for i in range(100)]
    def find(i):
        if tree[i] == i:
            return i
        else:
            tree[i]= find(tree[i])
            return find(tree[i])

    def union(a,b):
        if tree[a] > tree[b]:
            a,b = b,a
        #以下二行が各成分のサイズの処理
        if find(a)!=find(b):
            size[find(a)],size[find(b)]=size[find(b)]+size[find(a)],size[find(b)]+size[find(a)]
        tree[find(b)] = find(a)
    for i in range(9):
        for j in range(10):
            if box[i][j]==box[i+1][j] and box[i][j]!=0:
                union(10*i+j,10*(i+1)+j)
            if box[j][i]==box[j][i+1] and box[j][i]!=0:
                union(i+j*10,i+1+j*10)
    score = 0
    for i in range(100):
        score+=size[find(i)]
    return(score)
#pってどこ？
def search(box,p):
    cnt = 0
    for i in range(10):
        for j in range(10):
            if box[i][j]==0:
                cnt+=1
                if cnt==p:
                    return(i,j)
def move(box,dir):
    r = []
    if dir == "L" or dir == "R":
        for i in range(10):
            temp = []
            for j in range(10):
                if box[i][j]>0:
                    temp.append(box[i][j])
            temp2=[0 for j in range(10-len(temp))]
            if dir=="L":
                r.append(temp+temp2)
            else:
                r.append(temp2+temp)
        return(r)
    else:
        for j in range(10):
            temp = []
            for i in range(10):
                if box[i][j]>0:
                    temp.append(box[i][j])
            temp2=[0 for i in range(10-len(temp))]
            if dir=="F":
                r.append(temp+temp2)
            else:
                r.append(temp2+temp)
        r2 = [[r[i][j] for i in range(10)] for j in range(10)]
        return(r2)
#上下左右のうち一か所以上三か所以下が0であるものがどれくらいあるか？
def edge_check(mat):
    check = [0,0,0,0]
    for i in range(10):
        for j in range(10):
            cnt=0
            for d in [(0,-1),(0,1),(1,0),(-1,0)]:
                if 0<=i+d[0]<10 and 0<=j+d[1]<10:
                    if mat[i+d[0]][j+d[1]]==0:
                        cnt+=1
            if 1<=cnt<3:
                check[mat[i][j]]+=1
    return(check)
def four_sum(box,dir):
    global turn
    temp = move(box,dir)
    r = 0
    if 15<=turn<90:
        c = edge_check(temp)
        if c[f[turn+1]]<1:
            r-=10**4
        else:
            r+=3720*c[f[turn+1]]**(0.83)
    for d in ["L","R","F","B"]:
        r += caluculate(move(temp,d))**(1.25)
    return(r)

current = [[0 for i in range(10)] for j in range(10)]
for turn in range(100):
    p = int(input())
    x,y = search(current,p)
    current[x][y]=f[turn]
    cands = []
    cands.append((four_sum(current,"L"),"L"))
    cands.append((four_sum(current,"R"),"R"))
    cands.append((four_sum(current,"F"),"F"))
    cands.append((four_sum(current,"B"),"B"))
    cands.sort()
    print(cands[3][1])
    current = move(current,cands[3][1])
    sys.stdout.flush()

