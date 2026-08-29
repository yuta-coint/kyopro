N,K = map(int,input().split())
if N%2==0:
    print(-1)
    exit()
print((N-1)//2)
from math import gcd
g = gcd(N,K)
temp = 0
for i in range(N//(g*2)):
    print(temp,(temp+K)%N)
    temp+=K*2
    temp%=N
#gの倍数の奴らは全部連結された
back = N//g
def left(p):
    for i in range(g//2):
        print((p*K+i)%N,(p*K+i+1)%N)
def center(p):
    for i in range(g//2):
        print((p*K+i+1)%N,(p*K+i+1+g//2)%N)
def right(p):
    for i in range(g//2):
        print((p*K+g-i)%N,(p*K+g-1-i)%N)
left(0)
center(1)
right(2)
for j in range(3,back):
    if j&1:
        left(j)
    else:
        right(j)
