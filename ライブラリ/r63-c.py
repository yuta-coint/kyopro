N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
AB = [(A[i],B[i]) for i in range(N)]
AB.sort()
A = [AB[i][0] for i in range(N)]
B = [AB[i][1]+i*10**9 for i in range(N)]
print(N)
ans = []
print(1,A[N-1]+1)
A[N-1]=0
for i in range(N-1):
    A[i]+=1
for i in reversed(range(2,N)):
    x = B[i]-B[i-1]
    for j in range(N):
        A[j]+=x
    y = A[i-1]
    A[i-1]=0
    print(x,y)
ans.append((B[1]))