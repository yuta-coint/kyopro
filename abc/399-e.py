N = int(input())
SS = input()
TT = input()
S = []
T = []
for i in range(N):
    S.append(ord(SS[i])-ord("a"))
    T.append(ord(TT[i])-ord("a"))
henkan = [-1 for i in range(26)]
for i in range(N):
    if henkan[S[i]]==-1 or henkan[S[i]]==T[i]:
        henkan[S[i]] = T[i]
    else:
        print(-1)
        exit()
#基本的に合ってない文字の数だけ必要だが、孤立した非自明なサイクルが一つあるごとに、1手増え、そのような非自明なサイクルだけで、26字分あれば-1になる。
#連結成分に親が二つあるような頂点が無ければ、孤立したサイクルであることが分かる。孤立していないサイクル
chk = [False for i in range(26)]
ans = 0
for i in range(26):
    if henkan[i]!=i and henkan[i]!=-1:
        ans+=1
rev = [[] for i in range(26)]
for i in range(26):
    rev[henkan[i]].append(i)
temp = True
for i in range(26):
    if len(rev[i])!=1 or henkan[i]==i:
        temp = False
if temp and S!=T:
    print(-1)
    exit()
for i in range(26):
    if chk[i]:
        continue
    if henkan[i]==i:
        chk[i]=True
        continue
    t = i
    flag = False
    for _ in range(26):
        if t==-1:
            break
        if chk[t]:
            break
        chk[t] = True
        if len(rev[t])>=2:
            break
        t = henkan[t]
        if t==i:
            ans += 1
            break
print(ans)