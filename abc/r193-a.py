from bisect import bisect_left,bisect_right
N = int(input())
W = list(map(int,input().split()))
L_sort = []
R_sort = []
LR = []
for i in range(N):
    l,r = map(int,input().split())
    LR.append((l,r))
    L_sort.append((l,r,i))
    R_sort.append((r,l,i))
L_sort.sort(reverse=True)
R_sort.sort()
L_min = []
R_min = []
temp = 10**24
for i in range(N):
    if temp>W[L_sort[i][2]]:
        temp = W[L_sort[i][2]]
    L_min.append(temp)
temp = 10**24
for i in range(N):
    if temp>W[R_sort[i][2]]:
        temp = W[R_sort[i][2]]
    R_min.append(temp)
L_sort.reverse()
L_s = [L_sort[i][0] for i in range(N)]
R_s = [R_sort[i][0] for i in range(N)]
L_min.reverse()
L_min.append(10**24)
Q=int(input())
for _ in range(Q):
    s,t = map(int,input().split())
    s-=1
    t-=1
    if LR[s][1]<LR[t][0] or LR[t][1]<LR[s][0]:
        print(W[s]+W[t])
        continue
    ans = 10**24
    #右にいく
    key = max(LR[s][1],LR[t][1])
    b = bisect_left(L_s,key+1)
    temp = W[s]+W[t]+L_min[b]
    if ans>temp:
        ans = temp
    #左に行く
    key = min(LR[s][0],LR[t][0])
    b = bisect_right(R_s,key-1)
    if b==0:
        temp = 10**24
    else:
        temp = W[s]+W[t]+R_min[b-1]
    if ans>temp:
        ans = temp
    #左に行ってから右にいく
    temp = W[s]+W[t]
    key = LR[s][1]
    b = bisect_left(L_s,key+1)
    temp += L_min[b]
    key = LR[t][0]
    b = bisect_right(R_s,key-1)
    if b==0:
        temp = 10**24
    else:
        temp += R_min[b-1]
    if ans>temp:
        ans = temp
    #右に行ってから左にいく
    temp = W[s]+W[t]
    key = LR[t][1]
    b = bisect_left(L_s,key+1)
    temp += L_min[b]
    key = LR[s][0]
    b = bisect_right(R_s,key-1)
    if b==0:
        temp = 10**24
    else:
        temp += R_min[b-1]
    if ans>temp:
        ans = temp
    if ans == 10**24:
        print(-1)
    else:
        print(ans)
    