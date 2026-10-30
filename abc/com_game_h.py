N,M,K = map(int,input().split())
G = [set() for i in range(N)]
for i in range(M):
    u,v,c = input().split()
    u,v = int(u),int(v)
    G[u-1].add((v-1,ord(c)-ord("a")))
#print(G)
#何番目にアリスにとって有利な場所かを計算する。
optimal = [[0] * N for i in range(2 * K + 1)]
next_letter = [[0] * N for i in range(2 * K)]
for rem_turn in range(1,2 * K + 1):
    if rem_turn & 1:
        parity = -1
    else:
        parity = 1
    score = [0] * N
    for i in range(N):
        mi = 10**24
        nl = c
        for v,c in G[i]:
            hoge = c + optimal[rem_turn - 1][v] * 27
            hoge *= parity
            if hoge < mi:
                mi = hoge
                nl = (v,c)
        score[i] = (mi,i)
        next_letter[rem_turn - 1][i] = nl
    if parity == 1:
        score.sort()
    else:
        score.sort(reverse=True)
    #print(score)
    for i in range(N):
        if i > 0:
            if score[i][0] == score[i - 1][0]:
                optimal[rem_turn][score[i][1]] = optimal[rem_turn][score[i - 1][1]]
                continue
        optimal[rem_turn][score[i][1]] = i
#print(optimal)
ans = [0] * (2 * K)
now = 0
for i in range(2 * K):
    v,c = next_letter[2 * K - 1 - i][now]
    now = v
    ans[i] = chr(ord("a") + c)
ans.reverse()
print(*ans,sep = "")