N,M=map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
score = 0
for i in range(M):
    score+=A[B[i]-1]
print(score)