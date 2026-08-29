#大きさがKの倍数の部分がN個あればよい。
N,K  = map(int,input().split())
G = [[] for i in range(N*K)]
for i in range(N*K-1):
    u,v  = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
#Euler tourを作る#################################################
parent = [-1 for i in range(N*K)]

#帰りがけの順序を作る#################################################
parent = [-1 for i in range(N*K)]
is_bottom = [False for i in range(N*K)]
def backward(n, X, i0):
    done = [0] * n
    Q = [-i0-1, i0] # 根をスタックに追加
    bw = []
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            bottom = True
            for a in X[i][::-1]:
                if done[a]: continue
                parent[a]=i
                Q.append(~a) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加
                bottom =False
            if bottom:
                is_bottom[i]=True
        else: # 帰りがけの処理
            bw.append(~i)
    bw.pop()
    return bw

bwd = backward(N*K,G,0)

ans = "Yes"
#print(bwd)
size = [0 for i in range(N*K)]
for ii in range(len(bwd)):
    i = bwd[ii]
    #一個だけか、二個で足せるか
    amari = []
    cnt = 0
    for v in G[i]:
        if parent[i]==v:
            continue
        if size[v]==0:
            continue
        amari.append(size[v])
        cnt += 1
    if cnt>=3:
        ans = "No"
        break
    elif cnt==2:
        if amari[0]+amari[1]+1!=K:
            ans = "No"
            break
    elif cnt==1:
        size[i] = (amari[0]+1)%K
    else:
        size[i] = 1
    #print(i,size[i],amari)
print(ans)