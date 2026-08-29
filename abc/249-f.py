import sys
input=sys.stdin.readline
def main():
    N,K = map(int,input().split())
    op = []
    for i in range(N):
        t,y = map(int,input().split())
        op.append((t,y))
    plus = 0
    from heapq import heapify,heappop,heappush
    q=[]
    heapify(q)
    cnt =0
    ans = -float("inf")
    for i in range(N):
        t,y = op.pop()
        if t ==2:
            if y>=0:
                plus+=y
            else:
                heappush(q,-y)
                cnt+=1
                if cnt==K+1:
                    plus-=heappop(q)
                    cnt-=1
        else:
            ans = max(ans,plus+y)
            K-=1
            if K<0:
                break
            if cnt==K+1:
                plus-=heappop(q)
                cnt-=1
    else:
        ans = max(ans,plus)
    print(ans)
main()



