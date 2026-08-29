#Cが連続することはない
#となりが変われば一生変わらない
N = int(input())
CAND = list(input())
S = []
c = 0
for i in range(N):
    if CAND[i]=="A":
        t = 1
    else:
        t = -1
    if i==0:
        c=t
    else:
        S.append(t)
cum = [0]
for j in S:
    cum.append(cum[-1]+j)
ans = 1
for i in range(N-1):
    if cum[i]+c>0 and cum[i+1]>0:
        continue
    if cum[i]+c<0 and cum[i+1]<0:
        continue
    if cum[i]+c==0 and cum[i+1]==0:
        continue
    ans += 1
print(ans)