N = int(input())
A = [0]+list(map(int,input().split()))
d = {}
ans = []
for i in range(1,1+N):
    if A[i]==-1:
        ans.append(i)
    else:
        d[A[i]] = i
for i in range(N-1):
    ans.append(d[ans[-1]])
print(*ans)