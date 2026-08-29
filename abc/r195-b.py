N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
big = 10**12
A1 = []
cnt_A = {}
B1 = []
cnt_B = {}
for i in range(N):
    if A[i]==-1:
        continue
    if A[i] in cnt_A:
        A1.append(A[i]*big+cnt_A[A[i]])
        cnt_A[A[i]]+=1
    else:
        A1.append(A[i]*big)
        cnt_A[A[i]]=1
for i in range(N):
    if B[i]==-1:
        continue
    if B[i] in cnt_B:
        B1.append(B[i]*big-cnt_B[B[i]])
        cnt_B[B[i]]+=1
    else:
        B1.append(B[i]*big)
        cnt_B[B[i]]=1
S = len(A1)
T = len(B1)
if S+T<=N:
    print("Yes")
    exit()
U = N-S
V = N-T
ma = max(max(A1),max(B1))
A1.sort()
B1.sort()
cnt_sum = {}
for s in A1:
    for t in B1:
        if (s+t)%big!=0:
            continue
        if s+t in cnt_sum:
            cnt_sum[s+t]+=1
        else:
            cnt_sum[s+t]=1
M = 10**6
for u in cnt_sum:
    if u<ma-M:
        continue
    if S+T-cnt_sum[u]<=N:
        #print(u)
        print("Yes")
        exit()
print("No")