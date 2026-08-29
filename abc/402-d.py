N,M = map(int,input().split())
#和がmod Nで等しい。
wa = [0 for i in range(N)]
ans = M*(M-1)//2
for i in range(M):
    A,B = map(int,input().split())
    ans -= wa[(A+B)%N]
    wa[(A+B)%N] += 1
print(ans)