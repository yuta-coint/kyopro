N,M = map(int,input().split())
if N == 1:
    print(0)
elif N==2:
    print(4)
else:
    N-=1
    ans = N*(N-1)*(3*N*N+17*N+26)//24
    ans%=M
    for i in range(1,N+1):
        ans*=i
        ans%=M
    print(ans)
