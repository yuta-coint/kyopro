N = int(input())
P = list(map(int,input().split()))
key = -1

for i in reversed(range(1,N)):
    if P[i-1]>P[i]:
        key = i-1
        break
#print(key)
if key==N-2:
    P[N-1],P[N-2]=P[N-2],P[N-1]
    print(*P)
else:
    for i in reversed(range(key+1,N)):
        if P[key]>P[i]:
            temp = i
            break
    P[key],P[temp] = P[temp],P[key]
    Q = P[key+1:]
    Q.sort(reverse=True)
    print(*P[:key+1]+Q)
