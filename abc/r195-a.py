N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
best = []
worst = []
cnt = 0
for i in range(N):
    if cnt == M:
        break
    if A[i] == B[cnt]:
        cnt +=1
        best.append(i)
if cnt<M:
    print("No")
    exit()
cnt-=1
for i in reversed(range(N)):
    if cnt==-1:
        break
    if A[i] == B[cnt]:
        cnt -= 1
        worst.append(i)
worst.reverse()
if best == worst:
    print("No")
else:
    print("Yes")