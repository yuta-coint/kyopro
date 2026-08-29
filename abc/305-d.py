N = int(input())
A = list(map(int,input().split()))
sum_A = [0]
#print(sum_A)
for i in range(N//2):
    sum_A.append(sum_A[-1]+A[2*i+2]-A[2*i+1])
Q = int(input())
import bisect
for i in range(Q):
    l,r = map(int,input().split())
    t  = bisect.bisect(A,r)
    #print(t)
    ans = 0
    if t==0:
        pass
    elif t&1==0:
        ans += sum_A[(t-2)//2]+(r-A[t-1])
    else:
        ans += sum_A[t//2]
    t  = bisect.bisect(A,l)
    #print(t)
    if t==0:
        pass
    elif t&1==0:
        ans -= sum_A[(t-2)//2]+(l-A[t-1])
    else:
        ans -= sum_A[t//2]
    print(ans)