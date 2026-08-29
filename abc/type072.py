def TSP(rG,v,start):
    #i埋まり具合j居場所
    ans = [[0 for j in range(v)] for i in range(2**v)]
    #さしあたり0をしてとしてよい
    ans[1<<start][start]=1
    for i in range(1<<v):
        for j in range(v):
            if (i>>j)&1:
                for x in rG[j]:
                    if ans[i][j]<ans[i-(2**j)][x]:
                        ans[i][j]=ans[i-(2**j)][x]
    return(ans)
#64bit整数であれば、1になっているbitの数を求めることができる！
def popcount(n):
  c=(n&0x5555555555555555)+((n>>1)&0x5555555555555555)
  c=(c&0x3333333333333333)+((c>>2)&0x3333333333333333)
  c=(c&0x0f0f0f0f0f0f0f0f)+((c>>4)&0x0f0f0f0f0f0f0f0f)
  c=(c&0x00ff00ff00ff00ff)+((c>>8)&0x00ff00ff00ff00ff)
  c=(c&0x0000ffff0000ffff)+((c>>16)&0x0000ffff0000ffff)
  c=(c&0x00000000ffffffff)+((c>>32)&0x00000000ffffffff)
  return c
H,W = map(int,input().split())
c = []
for i in range(H):
    c+=list(input())
c_bit = 0
for i in range(H*W):
    if c[i]=="#":
        c_bit+=(1<<i)
G = [[] for i in range(H*W)]
for i in range(H-1):
    for j in range(W):
        G[i*W+j].append((i+1)*W+j)
        G[(i+1)*W+j].append(i*W+j)
for i in range(H):
    for j in range(W-1):
        G[i*W+j].append(i*W+j+1)
        G[i*W+j+1].append(i*W+j)
rG = [[] for i in range(H*W)]
for s in range(H*W):
    for t in G[s]:
        rG[t].append(s)
#print(routes)
#全ての部分集合について確認していきたい
ans = -1
#隣への移動ができますか？
for start in range(H*W):
    if c[start]=="#":
        continue
    routes = TSP(rG,H*W,start)
    #木がないことを確認
    for bits in range(1<<(H*W)):
        if bits&c_bit>0:
            continue
        #隣に行きつくことを考えればいい
        for i in G[start]:
            if routes[bits][i]==1:
                if ans <popcount(bits) and popcount(bits)>=3:
                    #print(bits,start)
                    ans = popcount(bits)
                break
print(ans)