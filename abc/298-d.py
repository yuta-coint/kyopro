Q = int(input())
from collections import deque
num = deque()
num.append(1)
s = 1
mod = 998244353
len_s = 0
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0]==1:
        x = query[1]
        s*=10
        s+=x
        s%=mod
        num.append(x)
        len_s+=1
    elif query[0]==2:
        head = num.popleft()
        s-=head*pow(10,len_s,mod)%mod
        s%=mod
        len_s-=1
    else:
        print(s)