N,M = map(int,input().split())
intervals = [10**8-M]
for i in range(N):
    L,R = map(int,input().split())
    intervals.append((10**9)*L+10**8-R)
intervals.sort(reverse=True)
rmax = M
lchecked = M
ans = 0
for i in range(N+1):
    L,R = intervals[i]//10**9,10**8-intervals[i]%(10**8)
    #lがL[i]より大きく、lchecked以下
    if lchecked<=rmax:
        ans += (lchecked - L)*(2*rmax-L-lchecked+1)//2
    elif L<rmax:
        ans += (rmax-L+1)*(rmax-L)//2
    #print(L,R,ans,lchecked,rmax)
    lchecked = L
    if R-1<rmax:
        rmax=R-1
print(ans)