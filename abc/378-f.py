N = int(input())
G = [[] for i in range(N)]
degree = [0 for i in range(N)]
for i in range(N-1):
    u,v = map(int,input().split())
    u-=1
    v-=1
    G[u].append(v)
    G[v].append(u)
    degree[u]+=1
    degree[v]+=1
ans = 0
cnt = [0]
white = [0 for i in range(N)]
#Euler tourを作る#################################################
parent = [-1 for i in range(N)]
def EulerTour(n, X, i0):
    global ans
    done = [0] * n
    Q = [-i0-1, i0] # 根をスタックに追加
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            #ET.append(i)
            for a in X[i][::-1]:
                if done[a]: continue
                parent[a]=i
                Q.append(~a) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加
        else: # 帰りがけの処理
            #ET.append(-i-1)
            if degree[-i-1]==3 and -i-1==i0:
                s,t,u = white[G[-i-1][0]],white[G[-i-1][1]],white[G[-i-1][2]]
                ans+= s*t+t*u+u*s
            elif degree[-i-1]==3:
                temp = 1
                for v in G[-i-1]:
                    if v == parent[-i-1]:
                        continue
                    #print(v,-i-1)
                    temp*=white[v]
                    white[-i-1] += white[v]
                ans += temp
            if degree[-i-1]==2:
                for v in G[-i-1]:
                    if v == parent[-i-1] or degree[v]!=3:
                        continue
                    ans+=white[v]
                white[-i-1]=1
                #print(-1-i,white[-i-1])
            #print(-i-1,ans)
    return 0
EulerTour(N,G,0)
##################################################################
#print(white)
#print(white[13],white[10])
print(ans)