N, K = map(int,input().split())
S = list(input())
countx = 0
for i in range(N):
    if S[i]=="X":
        countx+=1
if K>countx:
    for i in range(N):
        if S[i]=="X":
            S[i]="Y"
        else:
            S[i]="X"
    K=N-K
    countx=N-countx
if countx==N:
    print(max(K-1,0))
    exit()
if countx==N-1:
    print(K)
    exit()
ans = 0
for i in range(N-1):
    if S[i]=="Y" and S[i+1]=="Y":
        ans+=1
xseq = []
cnt = 10**9
for i in range(N):
    if S[i]=="Y":
        if cnt>0:
            xseq.append(cnt)
        cnt=0
    else:
        cnt+=1
xseq.sort()
#print(ans)
#print(xseq)
for i in range(len(xseq)):
    if K<xseq[i]:
        ans+=K
        break
    else:
        ans+=xseq[i]+1
        K-=xseq[i]
        if K<=0:
            break
print(ans)