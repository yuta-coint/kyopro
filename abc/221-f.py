import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline
MOD = 998244353
N =  int(input())
G=[[] for i in range(N+1)]
for i in range(N-1):
    s,t=map(int,input().split())
    G[s].append(t)
    G[t].append(s)
#for i in range(N+1):G[i].sort()
def dfs(v):
    global max_depth
    global depth
    global sea
    global mother
    global number_of_sea
    global check
    #global list_of_depth
    check[v]=1
    for i in G[v]:
        if check[i]==0:
            depth += 1
            if depth >= max_depth:
                max_depth = depth
                sea = i
            elif depth == max_depth//2:
                number_of_sea+=1
            #list_of_depth[i] = depth
            mother[i] = v
            dfs(i)
            depth -= 1
check=[0 for i in range(N+1)]
mother=[0 for i in range(N+1)]
#list_of_depth = [0 for i in range(N+1)]
check[1]=1
sea = 0
max_depth = 0
number_of_sea = 1
for i in G[1]:
    if max_depth<2:
        sea = i
    depth = 1
    dfs(i)
check=[0 for i in range(N+1)]
check[sea]=1
mother[sea] = 0
#list_of_depth[sea] = 0
for i in G[sea]:
    mother[i]=sea
    depth = 1
    #list_of_depth[i] = depth
    dfs(i)
#print(max_depth)
#print(mother)
#print(sea)
road_to_sea = [sea]
k = sea
for i in range(max_depth):
    k = mother[k]
    road_to_sea.append(k)
#print(road_to_sea)
ans = 1
check=[0 for i in range(N+1)]
if max_depth%2==0:
    root = road_to_sea[max_depth//2]
    check[root]=1
    nos = []
    for i in G[root]:
        number_of_sea = 0
        if max_depth == 2:
            number_of_sea+=1
        depth = 1
        dfs(i)
        nos.append(number_of_sea)
    #print(nos)
    for i in nos:
        ans *= i+1
        ans %= MOD
    ans -= sum(nos)
    ans -= 1
    ans %= MOD
else:
    root1 = road_to_sea[max_depth//2]
    root2 = road_to_sea[max_depth//2+1]
    #print(root1,root2)
    check[root1]=1
    check[root2]=1
    number_of_sea = 0
    for i in G[root1]:
        if i==root2:
            continue
        if max_depth == 3:
            number_of_sea+=1
            continue
        depth = 1
        dfs(i)
    ans *= number_of_sea
    ans %= MOD
    number_of_sea = 0
    check=[0 for i in range(N+1)]
    check[root1]=1
    check[root2]=1
    for i in G[root2]:
        #print(i)
        if i==root1:
            continue
        if max_depth == 3:
            number_of_sea+=1
            continue
        depth = 1
        dfs(i)
    #print(number_of_sea)
    ans *= number_of_sea
    ans %= MOD
if N==2:
    ans = 1
print(ans)
