a,b = map(int,input().split())
import math
g = math.gcd(a,b)
if (a*b)//g>10**18:
    print("Large")
else:
    print((a*b)//g)