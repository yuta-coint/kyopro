from collections import deque
Q = int(input())
uekibachi = deque()
plt = 0
day = 0
for _ in range(Q):
    q = list(input().split())
    if q[0]=="1":
        uekibachi.append(day)
        plt+=1
    elif q[0]=="2":
        day+=int(q[1])
    else:
        ans = 0
        if plt ==0:
            print(0)
            continue
        while uekibachi[0]<=day-int(q[1]):
            uekibachi.popleft()
            plt-=1
            ans+=1
            if plt==0:
                break
        print(ans)