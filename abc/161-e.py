N,K,C = map(int,input().split())
S = input()
fdp = [0 for i in range(N)]
rdp = [0 for i in range(N)]
#何日働けるか
last_work = -(N + 1)
day_work = 0
for i in range(N-1):
    if i > last_work + C and S[i] == "o":
        day_work += 1
        last_work = i
    fdp[i + 1] = day_work
next_work = 2 * N
day_work = 0
for i in reversed(range(1,N)):
    if next_work > i + C and S[i] == "o":
        day_work += 1
        next_work = i
    rdp[i - 1] = day_work
for i in range(N):
    if fdp[i] + rdp[i] < K:
        print(i + 1)
