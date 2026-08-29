import math
import sys
input = sys.stdin.readline
L,R = map(int,input().split())
ans = 0
for ab in range(1,R-L+1):
    ma = ((R//ab)-1)//2
    mi = (L-1)//(2*ab)+1
    for p in range(mi,ma+1):
        if ((2*p)*ab)^((2*p+1)*ab)==ab:
            ans+=1
print(ans)