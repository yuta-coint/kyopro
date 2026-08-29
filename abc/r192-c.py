import sys
input = sys.stdin.readline
N = int(input())
S1 = [0,0,0]
S2 = [0,0,0]
print("?",1,2)
sys.stdout.flush()
X = int(input())
S1[2] = X
S2[1] = X
for k in range(3,N+1):
    print("?",1,k)
    sys.stdout.flush()
    X = int(input())
    S1.append(X)
    print("?",2,k)
    sys.stdout.flush()
    X = int(input())
    S2.append(X)
M = 2
m = 1
for k in range(3,N+1):
    if S1[k]>S2[k]:
        if S1[k]>S1[M]:
            M = k
    if S1[k]<S2[k]:
        if S2[k]>S2[m]:
            m = k
if m == 1:
    temp = [(S1[k],k) for k in range(2,N+1)]
    temp.sort(reverse=True)
    A = []
    rP = []
    for i in range(N-2):
        A.append(temp[i][0]-temp[i+1][0])
        rP.append(temp[i][1])
    rP.append(temp[N-2][1])
    rP.append(1)
    print("?",temp[-1][1],temp[0][1])
    sys.stdout.flush()
    X = int(input())
    print("?",temp[-1][1],1)
    sys.stdout.flush()
    Y = int(input())
    A.append(X+Y-temp[0][0])
    A.append(temp[0][0]-X)
    A.reverse()
    rP.append(0)
    rP.reverse()
elif M == 2:
    temp = [(S2[k],k) for k in range(3,N+1)]
    temp.append((S2[1],1))
    temp.sort(reverse=True)
    A = []
    rP = [0]
    for i in range(N-2):
        A.append(temp[i][0]-temp[i+1][0])
        rP.append(temp[i][1])
    rP.append(temp[N-2][1])
    rP.append(2)
    print("?",temp[-1][1],temp[0][1])
    sys.stdout.flush()
    X = int(input())
    print("?",temp[-1][1],2)
    sys.stdout.flush()
    Y = int(input())
    A.append(X+Y-temp[0][0])
    A.append(temp[0][0]-X)
else:
    A = []
    Q = [0 for i in range(N+1)]
    Q[1] = S1[m]+S1[2]-S2[m]
    Q[2] = S1[2]+S2[M]-S1[M]
    right = []
    left = []
    center = []
    for k in range(3,N+1):
        if S1[k]+S1[2] == S2[k]+Q[1]:
            left.append((S1[k],k))
        elif S2[1]+S2[k] == S1[k]+Q[2]:
            right.append((S2[k],k))
        else:
            center.append((S1[k],k))
    #print(right,left,center)
    left.sort(reverse=True)
    left.append((Q[1],1))
    rP = [0]
    for i in range(1,len(left)):
        A.append(-left[i][0]+left[i-1][0])
        rP.append(left[i-1][1])
    A.append(Q[1])
    rP.append((1))
    center.append((Q[1],1))
    center.sort()
    for i in range(1,len(center)):
        A.append(center[i][0]-center[i-1][0])
        rP.append(center[i][1])
    A.append(Q[2])
    right.append((Q[2],2))
    rP.append((2))
    right.sort()
    for i in range(1,len(right)):
        A.append(-right[i-1][0]+right[i][0])
        rP.append(right[i][1])
P = [0 for i in range(N+1)]
for i in range(1,N+1):
    P[rP[i]] = i
ans = P+A
ans[0] = "!"
print(*ans)