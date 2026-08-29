A,B,M  = map(int,input().split())
#二つ目のヤング図形の種類をフック長の公式を用いて求める。
fac = [1]
for i in range(1,A*B):
    fac.append(fac[-1]*i%M)
ans_2 = fac[A*B-1]
ans_2_mother = 1
for x in range(A):
    for y in range(B):
        if x==0 and y==0:
            pass
        elif x==0 or y==0:
            ans_2_mother *= x+y
        else:
            ans_2_mother *= x+y+1
        ans_2_mother%=M
ans_2 = ans_2*pow(ans_2_mother,-1,M)%M
#print(ans_2)
#一つ目のヤング図形の種類が若干厄介
import itertools
dp = []
d = {}
i = 0
for r in itertools.combinations_with_replacement(range(A+1),B):
    d[r] = i
    i+=1
    if r[B-2]==0:
        if r[B-1]==A:
            dp.append(0)
        else:
            dp.append(1)
        continue
    score = 0
    for j in range(B):
        if r[j] == 0:
            continue
        if j>0:
            if r[j]==r[j-1]:
                continue
        s = list(r)
        s[j]-=1
        s = tuple(s)
        if s in d:
            score+=dp[d[s]]
            score%=M
    dp.append(score)
    #A-1が二連続してはいけないのがポイント
    mae = 10**9
    for j in r:
        if mae<A-1 and j==A:
            dp[-1]=0
        mae = j
dp.pop()
print(dp[-1]*ans_2%M)