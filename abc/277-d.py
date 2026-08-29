N,M = map(int,input().split())
A = list(map(int,input().split()))
cnt = {}
part = set()
S =0
for i in range(N):
    if A[i] in cnt:
        cnt[A[i]]+=A[i]
    else:
        cnt[A[i]]=A[i]
        part.add(A[i])
    S+=A[i]
temp = 0
ans = 0
pre = -1
for i in sorted(part):
    if i!=pre+1:
        temp = cnt[i]
    else:
        temp+=cnt[i]
    if ans<temp:
        ans=temp
    pre = i
for i in sorted(part):
    if i!=(pre+1)%M:
        temp = cnt[i]
    else:
        temp+=cnt[i]
    if ans<temp:
        ans=temp
    pre = i
if ans>S:
    print(0)
else:
    print(S-ans)