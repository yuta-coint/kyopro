from collections import deque
q = deque()
d = [-1]*(10**7)
d[1] = 0
q.append(1)
while q:
    v = q.popleft()
    cand = []
    if v%3 == 1 and (v//3) &1:
        cand.append(v//3)
    cand.append(v*2)
    for i in cand:
        if i >= 10**7:
            continue
        if d[i] == -1:
            d[i] = d[v] + 1
            q.append(i)
d = d[:10**6]
for i in range(1,10**6):
    if d[i] == -1:
        temp = i
        cnt = 0
        while temp > 1:
            if temp & 1:
                temp = temp * 3 + 1
            else:
                temp //= 2
            cnt += 1
        d[i] = cnt
                
print(d.index(max(d)))