N=int(input())
Balls = [tuple(map(int,input().split())) for i in range(N)]
data = [i for i in range(N)]
size = [1 for i in range(N)]
data_type = [[i] for i in range(N)]
history = [(-2,-2,0)]
def union(x,y):
    #xのやつをyに連れていく
    if size[data[x]]>size[data[y]]:
        x,y = y,x
    if data[x]==data[y]:
        history.append((-1,-1,0))
        return False
    history.append((x,y,size[data[x]]))
    sd = size[data[x]]
    size[data[y]]+=size[data[x]]
    size[data[x]]=0
    for i in range(sd):
        z = data_type[data[x]].pop()
        data_type[data[y]].append(z)
        data[z]=data[y]
    return True
def find(x):
    return data[x]
def roll_back():
    x,y,s = history.pop()
    if x==-2:
        history.append((x,y,s))
        return False
    for i in range(s):
        k = data_type[y].pop()
        data[k]=x
        data_type[x].append(k)
    size[y]-=s
    size[x]+=s
    if s>0:
        return True
    else:
        return False
G = [[] for i in range(N)]
for i in range(N-1):
    A,B = map(int,input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)
#Euler tourを作る#################################################
parent = [-1 for i in range(N)]

def EulerTour(n, X, i0):
    done = [0] * n
    Q = [-i0-1, i0] # 根をスタックに追加
    ET = []
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            ET.append(i)
            for a in X[i][::-1]:
                if done[a]: continue
                parent[a]=i
                Q.append(~i) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加

        else: # 帰りがけの処理
            ET.append(-i-1)
    ET.pop()
    return ET

Euler = EulerTour(N,G,0)
len_Euler = len(Euler)
##################################################################
ans = [-1 for i in range(N)]
#連結成分を数える
conn = N
for node in Euler:
    if ans[node]==-1:
        s,t = Balls[node]
        s-=1
        t-=1
        if union(s,t):
            conn-=1
        ans[node]=N-conn
        #print(node,data_type,s,t,data)
    else:
        if roll_back():
            conn+=1
print(*ans[1:])