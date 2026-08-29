T = int(input())
for case in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    S = sum(A)
    cnt = S//N
    ideal = [cnt for i in range(N)]
    for i in range(N-S%N,N):
        ideal[i]+=1
    ans = "Yes"
    cost = 0
    for i in range(N):
        cost+=A[i]-ideal[i]
        if cost>0:
            ans = "No"
            break
    print(ans)