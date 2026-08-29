N,Q = map(int,input().split())
A = list(map(int,input().split()))
mod = 998244353
temp = [[1,0,0,1] for j in range(N)]
for i in range(Q):
    X,Y = map(int,input().split())
    for j in range(N):
        if Y==0:
            temp[j][1]+=temp[j][0]
            temp[j][3]+=temp[j][2]
        else:
            temp[j][0]+=temp[j][1]
            temp[j][2]+=temp[j][3]
element = []
for j in range(N):
    t = []
    for i in range(2**N):
        if (i>>1)&1:
            t.append(temp[j][2]*A[i])
for i in range(2**N):


