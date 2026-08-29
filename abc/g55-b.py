from heapq import heapify,heappop,heappush
def main():
    N,X=map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    ans = A[-1]-A[0]
    q = [(A[-1],A[-1])]
    heapify(q)
    for i in range(N-1):
        cnt=0
        while 2*A[i]<=A[-1]:
            A[i]*=2
            cnt+=1
        B = A[i]+X*(2**cnt-1)
        #存在抹消できますか
        if B>=A[-1]:
            continue
        else:
            heappush(q,(B,A[i]))
    ma = A[-1]
    while True:
        s,t = heappop(q)
        if t == A[-1]:
            ans = min(ans,ma-s)
            break
        ans = min(ans,ma-s)
        t *=2
        s *=2
        s+=X
        ma = max(ma,t)
        if s<A[-1]:
            heappush(q,(s,t))
    if ans<X:
        print(0)
    else:
        print(ans)
main()