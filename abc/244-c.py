import sys
N = int(input())
chk = [0 for i in range(2*N+2)]
cnt = 1
aoki = 0
for i in range(N+1): 
    chk[aoki]=1
    while True:
        if chk[cnt]==0:
            print(cnt)
            sys.stdout.flush()
            cnt+=1
            break
        else:
            cnt+=1
    aoki = int(input())