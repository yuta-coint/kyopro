N,M = map(int,input().split())
S = input()
T = input()
#M=1は個別撃破
if M == 1:
    for i in range(N):
        if S[i]!=T[0]:
            print("No")
            exit()
    print("Yes")
#全部の操作を行うとみてよくて、いらない操作は最初にすればいい
from itertools import permutations
chk = list(permutations(range(M-1),M-1))
pat = len(chk)
chk_d = {chk[i]:i for i in range(pat)}
if S[0]!=T[0] or S[-1]!=T[-1]:
    print("No")
    exit()
dp = [False for i in range(pat)]
for i in range(pat):
    if chk[i][-1]==0:
        dp[i]=True
for i in range(1,N-1):
    new = [False for i in range(pat)]
    cnt = -1
    for sq in chk:
        cnt+=1
        if dp[cnt]==False:
            continue
        #curの長さはM-2
        cur = []
        for t in range(M-1):
            if sq[t]<M-2:
                cur.append(sq[t]+1)
        #一番最後に0をおけるか
        if T[0]==S[i]:
            new[chk_d[tuple(cur+[0])]]=True
        #一番最後以外に0をおけるか
        if T[sq[M-2]+1]==S[i]:
            for j in range(M-2):
                new[chk_d[tuple(cur[:j]+[0]+cur[j:])]]=True
            if sq[M-2]==M-2:
                new[chk_d[tuple(cur+[0])]]=True
    dp = new
    #print(dp)
for i in range(pat):
    if chk[i][-1]==M-2 and dp[i]:
        print("Yes")
        exit()
print("No")