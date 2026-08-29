N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
a46 = [0 for i in range(46)]
b46 = [0 for i in range(46)]
c46 = [0 for i in range(46)]
for i in range(N):
    a46[A[i]%46]+=1
    b46[B[i]%46]+=1
    c46[C[i]%46]+=1
ans = 0
for i in range(46):
    for j in range(46):
        ans+=a46[i]*b46[j]*c46[(-i-j)%46]
print(ans)