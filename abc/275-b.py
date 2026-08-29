A,B,C,D,E,F = map(int,input().split())
mod = 998244353
A%=mod
B%=mod
C%=mod
D%=mod
E%=mod
F%=mod
print(((A*B%mod*C%mod)-(D*E%mod*F%mod))%mod)
