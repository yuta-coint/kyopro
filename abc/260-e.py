import sys
input = sys.stdin.readline
N,M = map(int,input().split())
B = []
ma = -1
chk=[set() for i in range(M+1)]
for i in range(N):
    a,b = map(int,input().split())
    ma=max(ma,a)
    B.append(b)
    chk[a].add(i)
ran = [0 for i in range(M+2)]
brk = min(B)
#i:スタート
for i in range(1,brk+1):
    #print(ma)
    ran[ma-i+1]+=1
    ran[M-i+2]-=1
    for j in chk[i]:
        ma = max(B[j],ma)
#print(ran)
for i in range(1,M+1):
    ran[i]+=ran[i-1]
print(*ran[1:M+1])


