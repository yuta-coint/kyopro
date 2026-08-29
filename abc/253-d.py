N,A,B = map(int,input().split())
ans = (N*(N+1))//2
ans-= A*((N//A)*(N//A+1))//2
ans-= B*((N//B)*(N//B+1))//2
from math import gcd
C = (A*B)//gcd(A,B)
ans+=C*((N//C)*(N//C+1))//2
print(ans)