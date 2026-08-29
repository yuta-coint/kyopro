d = {}
s = []
N=int(input())
A = list(map(int,input().split()))
for i in range(N):
    if A[i] in d:
        d[A[i]]+=1
    else:
        d[A[i]]=1
        s.append(A[i])
s.sort(reverse=True)
ans = [0 for i in range(N)]
cnt = 0
for i in range(len(s)):
    ans[i]=d[s[i]]
for i in range(N):
    print(ans[i])