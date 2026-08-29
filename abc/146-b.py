def main():
    N,M,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    for b in reversed(range(31)):
        temp = 1<<b
        cand = []
        for i in range(N):
            if A[i]&temp==0:
                cand.append(temp-A[i])
            else:
                cand.append(0)
        cand.sort()
        cost = sum(cand[:K])
        if M>=cost:
            M-=cost
            ans+=temp
            for i in range(N):
                if A[i]&temp==0:
                    A[i]=0
                else:
                    A[i]-=temp
        else:
            for i in range(N):
                A[i]%=temp
    print(ans)
main()