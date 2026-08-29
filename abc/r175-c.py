N=  int(input())
vals= [tuple(map(int,input().split())) for i in range(N)]
#差ゼロが行けるか
lma = 0
rmi = 10**9
for i in range(N):
    if lma<vals[i][0]:
        lma = vals[i][0]
    if rmi>vals[i][1]:
        rmi = vals[i][1]
if rmi>=lma:
    print(*[lma for i in range(N)])
    exit()
#要らないところを捨てていく。
for i in reversed(range(N-1)):
    lp,rp = vals[i+1]
    lm,rm = vals[i]
    if lm>rp:
        rm = lm
    elif rm>rp:
        rm = rp
    vals[i],vals[i+1] = (lm,rm),(lp,rp)
ans = [vals[0][1]]
for i in range(1,N):
    if vals[i][0]<=ans[-1]<=vals[i][1]:
        ans.append(ans[-1])
    elif ans[-1]>vals[i][1]:
        ans.append(vals[i][1])
    else:
        ans.append(vals[i][0])
print(*ans)