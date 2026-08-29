N = int(input())
A = list(map(int,input().split()))
d = {}
B = []
for i in range(N):
    if A[i] in d:
        B.append(d[A[i]])
    else:
        B.append(-1)
    d[A[i]]=i+1
print(*B)