from math import isqrt
N=  int(input())
ans = 0
N//=2
while N>0:
    temp = isqrt(N)
    ans += (temp+1)//2
    N//= 2
print(ans)