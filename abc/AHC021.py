from copy import deepcopy
pyla = [list(map(int,input().split())) for i in range(30)]
pyla2 = deepcopy(pyla)
pyla_rev = [-1 for i in range(465)]
for i in range(30):
    for j in range(i+1):
        pyla_rev[pyla[i][j]]=(i,j)
pyla_rev2 = deepcopy(pyla_rev)
def check():
    for i in range(29):
        for j in range(i+1):
            if pyla[i][j]>pyla[i+1][j]:
                pyla[i][j],pyla[i+1][j] = pyla[i+1][j],pyla[i][j]
                return ((i,j,i+1,j))
            if pyla[i][j]>pyla[i+1][j+1]:
                pyla[i][j],pyla[i+1][j+1] = pyla[i+1][j+1],pyla[i][j]
                return ((i,j,i+1,j+1))
    return ((-1,-1,-1,-1))
def surge(x,y,x2,y2):
    ans.append((x,y,x2,y2))
    pyla_rev[pyla[x][y]],pyla_rev[pyla[x2][y2]]=pyla_rev[pyla[x2][y2]],pyla_rev[pyla[x][y]]
    pyla[x][y],pyla[x2][y2] = pyla[x2][y2],pyla[x][y]
def greedy(k):
    while True:
        i,j = pyla_rev[k]
        if i==0:
            break
        if j==0:
            if pyla[i-1][j]<pyla[i][j]:
                break
            else:
                surge(i-1,j,i,j)
        elif j==i:
            if pyla[i-1][j-1]<pyla[i][j]:
                break
            else:
                surge(i-1,j-1,i,j)
        else:
            if pyla[i][j]>pyla[i-1][j] and pyla[i][j]>pyla[i-1][j-1]:
                break
            elif pyla[i-1][j]>pyla[i-1][j-1]:
                surge(i,j,i-1,j)
            else:
                surge(i,j,i-1,j-1)
def down(k):
	while True:
		i,j = pyla_rev[k]
		if i==29:
			break
		if pyla[i+1][j]>pyla[i][j] and pyla[i+1][j+1]>pyla[i][j]:
			break
		elif pyla[i+1][j]>pyla[i+1][j+1]:
			surge(i,j,i+1,j+1)
		else:
			surge(i,j,i+1,j)
def sum_min(k):
    i,j = pyla_rev[k]
    if i==0:
        return 0
    elif j==0:
        if pyla[i-1][j]<k:
            return 0
    elif j==i:
        if pyla[i-1][j-1]<k:
            return 0
    else:
        if pyla[i-1][j]<k and pyla[i-1][j-1]<k:
            return 0
    q = []
    counting=[[0 for y in range(j+1)] for x in range(i-j+1)]
    lr = [[0 for y in range(j+1)] for x in range(i-j+1)]
    #とにかく少ない手数で大きいやつらを落としたい
    for x in reversed(range(i-j+1)):
        for y in reversed(range(j+1)):
            if x==i-j and y==j:
                continue
            if i-j==x:
                lr[x][y]=1
                counting[x][y]=counting[x][y+1]+pyla[x+y][y]
            elif y==j:
                counting[x][y] = counting[x+1][y]+pyla[x+y][y]
            else:
                if counting[x][y+1]>counting[x+1][y]:
                    lr[x][y]=1
                    counting[x][y]=counting[x][y+1]+pyla[x+y][y]
                else:
                    counting[x][y] = counting[x+1][y]+pyla[x+y][y]
    ideal = (0,0)
    ave = 0
    for x in range(i-j+1):
        for y in range(j+1):
            if x==i-j and y==j:
                continue
            if pyla[x+y][y]<k:
                continue
            flag = 0
            if x==0 and y==0:
                flag=1
            elif x==0:
                if pyla[x+y-1][y-1]<k:
                    flag =1
            elif y==0:
                if pyla[x+y-1][y]<k:
                    flag = 1
            else:
                if pyla[x+y-1][y-1]<k and pyla[x+y-1][y]<k:
                    flag = 1
            if flag==0:
                continue
            if counting[x][y]/(i-x-y)>ave:
                ideal = (x,y)
    z,w = ideal
    z+=w
    while z<i or w<j:
        q.append((z,w,z+1,w+lr[z-w][w]))
        w+=lr[z-w][w]
        z+=1
    q.reverse()
    for x0,y0,x1,y1 in q:
        surge(x0,y0,x1,y1)
ans = []
for i in range(465):
    greedy(i)
ans_max = deepcopy(ans)
for cut in range(150,350,2):
    ans = []
    pyla = deepcopy(pyla2)
    pyla_rev = deepcopy(pyla_rev2)
    for i in range(cut):
        greedy(i)
    for i in range(cut,465):
        sum_min(i)
    if len(ans)<len(ans_max):
        ans_max = deepcopy(ans)
ans = []
pyla = deepcopy(pyla2)
pyla_rev = deepcopy(pyla_rev2)
for k in range(465):
	for i in range(1,28):
		if pyla[i][0]<pyla[i+1][1]<pyla[i+2][0]<pyla[i][1]<pyla[i+1][0]:
			surge(i+1,0,i+1,1)
	for i in range(1,28):
		if pyla[i][i]<pyla[i+1][i]<pyla[i+2][i+2]<pyla[i][i-1]<pyla[i+1][i+1]:
			surge(i+1,i+1,i+1,i)
	greedy(k)
#print(len(ans))
if len(ans)<len(ans_max):
	ans_max = deepcopy(ans)
ans = []
pyla = deepcopy(pyla2)
pyla_rev = deepcopy(pyla_rev2)
for k in range(465):
	for i in range(1,28):
		if pyla[i][0]<pyla[i+1][1]<pyla[i+2][0]<pyla[i][1]<pyla[i+1][0]:
			surge(i+1,0,i+1,1)
	for i in range(1,28):
		if pyla[i][i]<pyla[i+1][i]<pyla[i+2][i+2]<pyla[i][i-1]<pyla[i+1][i+1]:
			surge(i+1,i+1,i+1,i)
	for i in range(2,27):
		for j in range(i-1):
			if pyla[i][j]<pyla[i+1][j+2]<pyla[i+2][j+1] and pyla[i][j+2]<pyla[i+1][j+1]<pyla[i+2][j+3] and ((pyla[i][j+2]>pyla[i+1][j+2] and pyla[i+1][j+1]>pyla[i+2][j+1]) or (pyla[i][j]>pyla[i+1][j+1] and pyla[i+1][j+2]>pyla[i+2][j+3])):
				surge(i+1,j+1,i+1,j+2)
	greedy(k)
#print(len(ans))
if len(ans)<len(ans_max):
	ans_max = deepcopy(ans)
ans = []
pyla = deepcopy(pyla2)
pyla_rev = deepcopy(pyla_rev2)
for k in reversed(range(465)):
	for i in range(1,28):
		if pyla[i][0]<pyla[i+1][1]<pyla[i+2][0]<pyla[i][1]<pyla[i+1][0]:
			surge(i+1,0,i+1,1)
	for i in range(1,28):
		if pyla[i][i]<pyla[i+1][i]<pyla[i+2][i+2]<pyla[i][i-1]<pyla[i+1][i+1]:
			surge(i+1,i+1,i+1,i)
	for i in range(2,27):
		for j in range(i-1):
			if pyla[i][j]<pyla[i+1][j+2]<pyla[i+2][j+1] and pyla[i][j+2]<pyla[i+1][j+1]<pyla[i+2][j+3] and ((pyla[i][j+2]>pyla[i+1][j+2] and pyla[i+1][j+1]>pyla[i+2][j+1]) or (pyla[i][j]>pyla[i+1][j+1] and pyla[i+1][j+2]>pyla[i+2][j+3])):
				surge(i+1,j+1,i+1,j+2)
	down(k)
if len(ans)<len(ans_max):
	ans_max = deepcopy(ans)
print(len(ans_max))
for s,t,w,v in ans_max:
    print(s,t,w,v)