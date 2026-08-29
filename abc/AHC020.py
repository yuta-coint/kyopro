#周辺にいっぱいある頂点の出力強度を上げたい
#周辺にあんまりない頂点は必要以上に採択したくない
#頂点決めて、そこからできる限り最適化したい
from sys import setrecursionlimit
setrecursionlimit(10**7)
def Kruskal(graph,v,e):
    tree = [i for i in range(v)]
    def find(i):
        if tree[i] == i:
            return i
        else:
            tree[i]= find(tree[i])
            return find(tree[i])
 
    def union(a,b):
        if tree[a] > tree[b]:
            a,b = b,a
        tree[find(b)] = find(a)
    graph.sort()
    ans = 0
    mst = [0 for i in range(e)]
    for cost,edgel,edger,ind in graph:
        #print(tree)
        if find(edgel)!=find(edger):
            union(edgel,edger)
            ans += cost
            mst[ind]=1
    return(mst)
 
N,M,K  = map(int,input().split())
def evaluate(P,B):
    score = 0
    for i in range(N):
        score+=P[i]*P[i]
    for i in range(M):
        score+=B[i]
    return score
G_mat = [[0 for j in range(N)] for i in range(N)]
G = [[] for i in range(N)]
vertexs = [tuple(map(int,input().split())) for i in range(N)]
edges = []
for i in range(M):
    u,v,w = map(int,input().split())
    edges.append((w,u-1,v-1,i))
citizens = [tuple(map(int,input().split())) for i in range(K)]
#とりあえず全部動く感じにしたい
#各々の市民にとって一番近いやつを考える
#各住民がどの頂点をよりどころにしているか
B = Kruskal(edges,N,M)
dependant = []
from math import sqrt,ceil
P = [0 for i in range(N)]
maxP = [0 for i in range(N)]
from random import shuffle
rdk = [i for i in range(N)]
score = 10**24
for _ in range(60):
	P = [0 for i in range(N)]
	shuffle(rdk)
	for x,y in citizens:
		nearest = -1
		near_dist = 10**16
		for i in rdk:
			x0,y0 = vertexs[i]
			#そもそもすでに受信できてるやつは問答無用で除去する。
			if P[i]**2>(x-x0)**2+(y-y0)**2:
				near_dist = (x-x0)**2+(y-y0)**2
				nearest=i
				break
			if (x-x0)**2+(y-y0)**2<near_dist:
				near_dist = (x-x0)**2+(y-y0)**2
				nearest = i
		dependant.append(nearest)
		if P[nearest]**2<near_dist:
			P[nearest]=ceil(sqrt(near_dist+300000))
	def dist(man,sate):
		return ceil(sqrt((citizens[man][0]-vertexs[sate][0])**2+(citizens[man][1]-vertexs[sate][1])**2))
	realP = [0 for i in range(N)]
	for i in range(K):
		if realP[dependant[i]]<dist(i,dependant[i]):
			realP[dependant[i]]=dist(i,dependant[i])
	if score>evaluate(realP,B):
		maxP = realP
		score = evaluate(realP,B)
P = maxP
#0の葉は抜く
dimention = [0 for i in range(N)]
edges.sort(key=lambda val: val[3])
for i in range(M):
    if B[i]==1:
        dimention[edges[i][1]]+=1
        dimention[edges[i][2]]+=1
def leaf_cutting():
	for i in range(M):
		if edges[i][1]==0 or edges[i][2]==0:
			continue
		#if i==86:
		#	print(dimention[edges[i][1]],dimention[edges[i][2]])
		if B[i]==1:
			if dimention[edges[i][1]]==1 and P[edges[i][1]]==0:
				B[i]=0
				dimention[edges[i][1]]-=1
				dimention[edges[i][2]]-=1
		if B[i]==1:
			if dimention[edges[i][2]]==1 and P[edges[i][2]]==0:
				B[i]=0
				dimention[edges[i][1]]-=1
				dimention[edges[i][2]]-=1
for _ in range(10):
    leaf_cutting()
count_dependant = [0 for i in range(N)]
list_dependant = [[] for i in range(N)]
for i in range(K):
    count_dependant[dependant[i]]+=1
    list_dependant[dependant[i]].append(i)
#どこまで頑張ればカバーできるか
def mountain_leaf_cutting():
    for i in range(M):
        if edges[i][1]==0 or edges[i][2]==0:
            continue
        if B[i]==0:
            continue
        if dimention[edges[i][1]]!=1 and dimention[edges[i][2]]!=1:
            continue
        if dimention[edges[i][1]]==1:
            j = edges[i][1]
            k = edges[i][2]
        else:
            j = edges[i][2]
            k = edges[i][1]
        if count_dependant[j]>=10:
            continue
        #jに依存している奴らの依存先をkにすることには意味があるか？
        newpk = P[k]
        for dpn in list_dependant[j]:
            if dist(dpn,k)>newpk:
                newpk = dist(dpn,k)
        score_diff = newpk**2-P[k]**2-P[j]**2-edges[i][0]
        #if i==134:
        #    print(i,j,k,newpk)
        if score_diff<0:
            B[i]=0
            P[j]=0
            P[k]=newpk
            list_dependant[k]=list_dependant[k]+list_dependant[j]
            list_dependant[j]=[]
            count_dependant[k]+=count_dependant[j]
            count_dependant[j]=0
            dimention[j]-=1
            dimention[k]-=1
def mountain_leaf_cutting2():
    for i in range(M):
        if edges[i][1]==0 or edges[i][2]==0:
            continue
        if B[i]==0:
            continue
        if dimention[edges[i][1]]!=1 and dimention[edges[i][2]]!=1:
            continue
        if dimention[edges[i][1]]==1:
            j = edges[i][1]
            k = edges[i][2]
        else:
            j = edges[i][2]
            k = edges[i][1]
        #kも消せるならjの依存先を変える
        if dimention[k]!=2 or P[k]>0:
            continue
        
for i in range(10):
    #print(B[134])
    mountain_leaf_cutting()
for i in range(3):
    leaf_cutting()
for i in range(3):
    #print(B[134])
    mountain_leaf_cutting()
for i in range(3):
    leaf_cutting()
print(*P)
print(*B)
#print(evaluate(P,B))
