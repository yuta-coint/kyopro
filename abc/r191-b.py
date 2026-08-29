T = int(input())
for case in range(T):
    N,K = map(int,input().split())
    bits = []
    while N>0:
        bits.append(N&1)
        N//=2
    cap=bits.count(0)
    if K>(1<<cap):
        print(-1)
    else:
        K-=1
        ans = 0
        for i in range(len(bits)):
            if bits[i]==0:
                bits[i]=K&1
                K//=2
            if bits[i]==1:
                ans+=1<<i
        print(ans)