H,W = map(int,input().split())
S = [list(input()) for i in range(H)]
ans = 1
mod = 998244353
#-1:空席 0:赤 1:青
chk = [-1 for i in range(H + W - 1)]
#.の存在
emp = [0 for i in range(H + W - 1)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "R":
            if chk[i+j] == 1:
                print(0)
                exit()
            elif chk[i+j] == -1:
                chk[i+j] = 0
        elif S[i][j] == "B":
            if chk[i+j] == 0:
                print(0)
                exit()
            elif chk[i+j] == -1:
                chk[i+j] = 1
        else:
            emp[i+j] = 1
for i in range(H + W - 1):
    if chk[i] == -1 and emp[i] == 1:
        ans *= 2
        ans %= mod
print(ans)

