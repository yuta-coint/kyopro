N1, K1 = map(int,input().split())
p0 = list(map(int,input().split()))
def solve(N,n,p,s):
    LIS = [(-1,0)]
    #rotateさせる
    #print(p)
    for i in range(N):
        a = p[i]
        if n == 0 and LIS[-1][1]==1:
            LIS.append((a,1))
            continue
        while LIS[-1][0]>p[i]:
            n-=LIS.pop()[1]
            if n==0 and LIS[-1][1]==1:
                break
        if i<s:
            LIS.append((a,0))
        else:
            LIS.append((a,1))
    ans = [i[0] for i in LIS]
    ans = ans[1:]
    #print(ans)
    for _ in range(n):
        ans.pop()
    return(ans)
answ = [float('inf')]
if K1!=0:
    start = min(p0[N1-K1:])
    t = p0.index(start)
    answ = solve(N1,K1-(N1-t),p0[t:]+p0[:t],N1-t)
start = min(p0[:K1+1])
t = p0.index(start)
#print(solve(N1-t,K1-t,p0[t:],1))
answ = min(answ,solve(N1-t,K1-t,p0[t:],0))
print(*answ)