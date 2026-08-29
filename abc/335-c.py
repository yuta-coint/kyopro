N,Q = map(int,input().split())
parts = [(i,0) for i in reversed(range(1,N+1))]
temp = N
for q in range(Q):
    n,C = input().split()
    if n == "1":
        x,y= parts[-1]
        if C == "R":
            parts.append((x+1,y))
        elif C == "L":
            parts.append((x-1,y))
        elif C=="U":
            parts.append((x,y+1))
        elif C=="D":
            parts.append((x,y-1))
        temp+=1
    else:
        print(parts[temp-int(C)])