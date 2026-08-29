N = int(input())
ans = [[0 for i in range(N)] for j in range(N)]
m=1
M=N*N
if N&1:
    med=(N-1)>>1
    med2=(N-1)>>1
else:
    med=(N-1)>>1
    med2=N>>1
for i in range(N):
    for j in range(N):
        if max(abs(i-med),abs(j-med),abs(j-med2),abs(i-med2))&1:
            ans[i][j]=m
            m+=1
        else:
            ans[i][j]=M
            M-=1
for i in range(N):
    print(*ans[i])