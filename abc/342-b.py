N = int(input())
P = list(map(int,input().split()))
rP = [0 for i in range(N)]
for i in range(N):
    rP[P[i]-1] = i
Q = int(input())
for i in range(Q):
    a,b = map(int,input().split())
    if rP[a-1]<rP[b-1]:
        print(a)
    else:
        print(b)
