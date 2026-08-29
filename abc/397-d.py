from math import sqrt
N=  int(input())
for sa in range(1,10**6):
    seki = N-sa**3
    if seki%(3*sa)!=0 or seki<=0:
        continue
    seki//=(3*sa)
    D = sa**2+4*seki
    rD = int(sqrt(D)//1)
    if D!=rD*rD:
        continue
    if (rD-sa)%2!=0:
        continue
    y = (rD-sa)//2
    x = y+sa
    if x<=0 or y<=0:
        continue
    print(x,y)
    exit()
print(-1)