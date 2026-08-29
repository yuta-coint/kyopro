H,W = map(int,input().split())
S = [list(input()) for i in range(H)]
ans = 0
for h2 in range(H):
    for h1 in range(h2 + 1):
        for w2 in range(W):
            for w1 in range(w2 + 1):
                cnt = 1
                for i in range(h1,h2 + 1):
                    for j in range(w1, w2 + 1):
                        if S[i][j] != S[h1 + h2 - i][w1 + w2 - j]:
                            cnt = 0
                ans += cnt
print(ans)