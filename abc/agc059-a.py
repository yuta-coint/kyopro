
N,Q = map(int,input().split())
S = list(input())
import sys
input = sys.stdin.readline
A = [0]
B = [0]
C = [0]
p,q,r = 0,0,0
compress = [S[0]]
d = [1]
cnt =1
for i in range(1,N):
    if compress[-1]==S[i]:
        d.append(cnt)
    else:
        compress.append(S[i])
        cnt+=1
        d.append(cnt)
for i in range(cnt):
    if compress[i]=="A":
        p+=1
    elif compress[i]=="B":
        q+=1
    else:
        r+=1
    A.append(p)
    B.append(q)
    C.append(r)
#print(compress)
#print(d)
#print(A)
#print(B)
#print(C)
for _ in range(Q):
    L,R = map(int,input().split())
    L,R =d[L-1],d[R-1]
    if compress[L-1]==compress[R-1]:
        print((R-L+1)//2)
    else:
        print((R-L+2)//2)
