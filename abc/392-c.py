N = int(input())
P = [0]+list(map(int,input().split()))
Q = [0]+list(map(int,input().split()))
#i が書かれたゼッケンを着けている人
step1 = [0 for i in range(N+1)]
for i in range(1,N+1):
    step1[Q[i]] = i
step2 = [0 for i in range(N+1)]
for i in range(1,N+1):
    step2[i] = Q[P[step1[i]]]
print(*step2[1:N+1])
