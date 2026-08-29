mod = 998244353
#各S_{k}を含む良い集合を数えればよい
N = int(input())
d = [0 for i in range(10**6)]
son = [0 for i in range(10**6)]
d[0] = 0
ed = set()
pow2 = [1]
for i in range(10**6):
    pow2.append(pow2[-1]*2%mod)
Ss = [input() for i in range(N)]
cnt = 3
keys = [[0] for i in range(N)]
H = [-1 for i in range(10**6)]
M = [-1 for i in range(10**6)]
H[0] = 1
M[0] = 2
for j in range(N):
    S = Ss[j]
    L = len(S)
    cur = 0
    for i in range(L):
        if S[i] == "A":
            if H[cur] == -1:
                H[cur] = cnt
                cnt += 1
            cur = H[cur]
        else:
            if M[cur] == -1:
                M[cur] = cnt
                cnt += 1
            cur = M[cur]
        keys[j].append(cur)
for j in range(N):
    S = Ss[j]
    L = len(S)
    X = keys[j][-1]
    ed.add(X)
    #print(X)
    for k in reversed(range(L+1)):
        X = keys[j][k]
        son[X] += 1
        temp = 0
        if H[X]!=-1 and M[X]!=-1:
            temp = H[X]*M[X]%mod
        if X in ed:
            temp += pow2[son[X]-1]
            temp %= mod
        d[X] = temp
    print(d[0])