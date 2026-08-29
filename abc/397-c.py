N=  int(input())
A = list(map(int,input().split()))
S = set()
H = []
cnt = 0
for i in range(N-1):
    if A[i] in S:
        pass
    else:
        cnt+=1
        S.add(A[i])
    H.append(cnt)
S = set()
cnt = 0
T = []
for i in reversed(range(1,N)):
    if A[i] in S:
        pass
    else:
        cnt+=1
        S.add(A[i])
    T.append(cnt)
T.reverse()
ans = []
for i in range(N-1):
    ans.append(H[i]+T[i])
print(max(ans))