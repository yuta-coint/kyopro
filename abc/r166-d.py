INF = 10**24
N = int(input())
x = list(map(int,input().split()))
x.append(INF)
y = list(map(int,input().split()))
R = []
L = []
cnt = 0
for i in reversed(range(N)):
    if cnt<y[i]:
        R.append((x[i+1]-1,y[i]-cnt))
        cnt = y[i]
    elif cnt>y[i]:
        L.append((x[i]+1,cnt-y[i]))
        cnt = y[i]
ans = 10**24
R.reverse()
L.reverse()
while L and R:
    L1,cl = L.pop()
    R1,cr = R.pop()
    if ans>R1-L1:
        ans = R1-L1
    if cl>cr:
        L.append((L1,cl-cr))
    elif cl<cr:
        R.append((R1,cr-cl))
if ans>10**13:
    print(-1)
else:
    print(ans)

