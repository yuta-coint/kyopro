#番号の付いた30こを11この入れ物に入れる方法
n = 30
k = 11
#全員コンプリート

def pcq(p,q):
    com = 1
    for i in range(q):
        com *= p-i
        com //=i+1
    return(com)
ans = 0
for i in range(1,k+1):
    temp = (-1)**(k-i)
    temp*=pcq(k,i)
    temp*=i**n
    ans+=temp
print(ans/k**n)

mod = 10**9+7
n,k = map(int,input().split())
partition = [[0 for j in range(k+1)] for i in range(n+1)]
for i in range(n+1):
    for j in range(k+1):
        if i==0 or j==1:
            partition[i][j]=1
        elif j==0:
            continue
        elif i<j:
            partition[i][j]=partition[i][j-1]
        else:
            partition[i][j] = (partition[i-j][j]+partition[i][j-1])%mod
print(partition[n][k])

mod = 10**9+7
n,k = map(int,input().split())
partition = [[0 for j in range(k+1)] for i in range(n+1)]
for i in range(n+1):
    for j in range(k+1):
        if i==0 or j==1:
            partition[i][j]=1
        elif j==0:
            continue
        elif i<j:
            partition[i][j]=partition[i][j-1]
        else:
            partition[i][j] = (partition[i-j][j]+partition[i][j-1])%mod
if n<k:
    print(0)
else:
    print(partition[n-k][k])
