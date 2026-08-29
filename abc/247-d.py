from collections import deque
q = int(input())
box = deque([])
for i in range(q):
    query = list(map(int,input().split()))
    if query[0]==1:
        x,c=query[1],query[2]
        box.append((x,c))
    else:
        s = query[1]
        ans = 0
        while True:
            x,c = box.popleft()
            if s>c:
                ans+=x*c
                s-=c
            else:
                ans+=x*s
                box.appendleft((x,c-s))
                break
        print(ans)

