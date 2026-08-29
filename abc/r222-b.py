T = int(input())
for _ in range(T):
    a,b,c = map(int,input().split())
    ans = 0
    cand = [0]
    if a == 0:
        if b > c:
            cand.append(c-1)
        else:
            cand.append(b)
    if b == 0:
        if c > a:
            cand.append(a-1)
        else:
            cand.append(c)
    if c == 0:
        if a > b:
            cand.append(b - 1)
        else:
            cand.append(a)
    cand.append(min(a+b-1,c-1))
    cand.append(min(b+c-1,a-1))
    cand.append(min(c+a-1,b-1))
    if a-1 > b + c - 2:
        cand.append(b+c-2)
    elif b-1>a+c-2:
        cand.append(a+c-2)
    elif c-1>a+b-2:
        cand.append(a+b-2)
    else:
        cand.append((a+b+c-3)//2)
    print(max(cand))