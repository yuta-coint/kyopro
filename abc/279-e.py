N,M = map(int,input().split())
A = list(map(int,input().split()))
skip = []
B = [j for j in range(N)]
for i in range(M):
    B[A[i]],B[A[i]-1]=B[A[i]-1],B[A[i]]
    if B[A[i]-1]==0:
        skip.append(B[A[i]])
    elif B[A[i]]==0:
        skip.append(B[A[i]-1])
    else:
        skip.append(0)
#print(B)
#print(skip)
index = [-1 for i in range(N)]
for j in range(N):
    index[B[j]]=j
for j in range(M):
    print(index[skip[j]]+1)
    