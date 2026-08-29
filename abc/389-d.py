from math import sqrt,floor
R = int(input())
ans = 1+(R-1)*4
R*=2
for r in range(1,10**6+83):
    if R**2-(2*r+1)*(2*r+1)<=0:
        break
    t = floor(sqrt(R**2-(2*r+1)*(2*r+1)))-1
    if t>0:
        ans+=(t//2)*4
print(ans)