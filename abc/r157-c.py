H,W = map(int,input().split())
S = [list(input()) for i in range(H)]
mod = 998244353
route = [[0 for i in range(W)] for j in range(H)]
pat = [[0 for i in range(W)] for j in range(H)]
pat_rev = [[0 for i in range(W)] for j in range(H)]
ans = 0
if H==1:
    for j in range(1,W):
        if S[0][j-1]=="Y" and S[0][j]=="Y":
            ans+=1
    print(ans*ans%mod)
    exit()

if W==1:
    for i in range(1,H):
        if S[i][0]=="Y" and S[i-1][0]=="Y":
            ans+=1
    print(ans*ans%mod)
    exit()

for j in range(W):
    route[0][j]=1
for i in range(H):
    route[i][0]=1
    for j in range(1,W):
        route[i][j]=(route[i-1][j]+route[i][j-1])%mod

for i in range(H):
    for j in range(W):
        if j>0:
            pat[i][j]+=pat[i][j-1]
            if S[i][j]=="Y" and S[i][j-1]=="Y":
                pat[i][j]+=route[i][j-1]
        if i>0:
            pat[i][j]+=pat[i-1][j]
            if S[i][j]=="Y" and S[i-1][j]=="Y":
                pat[i][j]+=route[i-1][j]
        pat[i][j]%=mod

for i in reversed(range(H)):
    for j in reversed(range(W)):
        if j<W-1:
            pat_rev[i][j]+=pat_rev[i][j+1]
            if S[i][j]=="Y" and S[i][j+1]=="Y":
                pat_rev[i][j]+=route[H-1-i][W-j-2]
        if i<H-1:
            pat_rev[i][j]+=pat_rev[i+1][j]
            if S[i][j]=="Y" and S[i+1][j]=="Y":
                pat_rev[i][j]+=route[H-2-i][W-j-1]
        pat_rev[i][j]%=mod

for i in range(1,H):
    for j in range(W):
        if S[i][j]=="Y" and S[i-1][j]=="Y":
            ans+=pat[i-1][j]*route[H-1-i][W-1-j]%mod
            ans%=mod
            ans+=pat_rev[i][j]*route[i-1][j]%mod
            ans%=mod
            ans+=route[H-1-i][W-1-j]*route[i-1][j]%mod
            ans%=mod
for i in range(H):
    for j in range(1,W):
        if S[i][j]=="Y" and S[i][j-1]=="Y":
            ans+=pat[i][j-1]*route[H-1-i][W-1-j]%mod
            ans%=mod
            ans+=pat_rev[i][j]*route[i][j-1]%mod
            ans%=mod
            ans+=route[H-1-i][W-1-j]*route[i][j-1]%mod
            ans%=mod
print(ans)