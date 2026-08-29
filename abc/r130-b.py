import sys
input = sys.stdin.readline
h,w,C,q = map(int,input().split())
lq=[list(map(int,input().split())) for i in range(q)]
press = []
for i in range(q):
    press.append(lq[i][1])
press.sort()
press = list(set(press))
dict={press[i]:i for i in range(len(press))}
for i in range(q):
    lq[i][1]=dict[lq[i][1]]
ans = [0 for i in range(C)]
check1 = [0 for i in range(q)]
check2 = [0 for i in range(q)]
rh = h
rw = w
for i in reversed(range(q)):
    t,n,c = lq[i][0],lq[i][1],lq[i][2]
    c-=1
    if t ==1:
        if check1[n]==1:
            continue
        check1[n]=1
        ans[c]+=rw
        rh-=1
    if t==2:
        if check2[n]==1:
            continue
        check2[n]=1
        ans[c]+=rh
        rw-=1
print(*ans)

