import copy
n,k = map(int,input().split())
s = list(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
a1 = {alpha[i]:i for i in range(26)}
ra1 = {i:alpha[i] for i in range(26)}
s = [a1[s[i]] for i in range(n)]
ideal = sorted(s)
coin = [2 for i in range(n)]
for i in range(n):
    if s[i]==ideal[i]:
        coin[i]=0
temp = []
maxd = 0
for i in range(n):
    if coin[i]==0:
        maxd+=1
        continue
    temp.append(ideal[i])
    temp_coin = copy.copy(coin)
    #print(temp)
    for j in range(i+1):
        if s[j] in temp and coin[j]==2:
            coin[j]=1
    dist = 0
    for j in range(i+1):
        dist+=coin[j]
    if dist>k:
        coin = temp_coin
        break
    else:
        maxd+=1
ans = copy.copy(s)
#print(coin)
#print(maxd)
#もともとaがあった場所に入れられるべきもの
candidate = [[] for i in range(26)]
lcan = [0 for i in range(26)]
for i in range(maxd):
    if coin[i]==2:
        candidate[ideal[i]].append(ans[i])
        lcan[ideal[i]]+=1
check = [0 for i in range(26)]
#もともとaがあった場所
space = [[] for i in range(26)]
for i in range(maxd,n):
    space[ans[i]].append(i)
    if check[ans[i]]<lcan[ans[i]]:
        check[ans[i]]+=1
    else:
        candidate[ans[i]].append(ans[i])
print(candidate)
print(space)
for i in range(26):
    candidate[i].sort
    for j in range(len(candidate[i])):
        ans[space[i][j]] = candidate[i][j]
for i in range(maxd):
    ans[i] = ideal[i]
ans = [ra1[ans[i]] for i in range(n)]
print(*ans,sep="")