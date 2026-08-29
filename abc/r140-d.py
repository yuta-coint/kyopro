import sys
input = sys.stdin.readline
##mの(pow乗)
def bigpower(base,pow):
    num = 1
    for i in reversed(range(len(bin(pow)))):
        num = num*num%mod
        if pow>>i & 1:
            num = num*base%mod
        i+=1
    return(num)
N = int(input())
A = list(map(int,input().split()))
n=N+1
tree = [i for i in range(n)]
size = [1 for i in range(n)]
sys.setrecursionlimit(10**6)
def find(i):
    if tree[i] == i:
        return i
    else:
        tree[i]= find(tree[i])
        return find(tree[i])

def union(a,b):
    if tree[a] > tree[b]:
        a,b = b,a
    #以下二行が各成分のサイズの処理
    if find(a)!=find(b):
        size[find(a)],size[find(b)]=size[find(b)]+size[find(a)],size[find(b)]+size[find(a)]
    tree[find(b)] = find(a)
mod = 998244353
death = []
free = 0
for i in range(1,N+1):
    if A[i-1]>0:
        if find(i)==find(A[i-1]):
            death.append(find(i))
        union(i,A[i-1])
    else:
        free+=1
F = free
teams = []
live=[1 for i in range(N+1)]
for i in death:
    live[find(i)]=0
for i in range(1,N+1):
    if find(i)==i:
        teams.append((size[i],live[i]))
T = len(teams)
ans = T*(bigpower(N,free))%mod
#iがjと繋がってるパターンが何通りか
pat = [[0 for j in range(T)] for i in range(T)]
for i in range(T):
    pat[i][i]=teams[i][0]
for i in range(T):
    if teams[1]==0:
        continue
    else:
        #各場所からの矢印で何個減らせるかな？
        free-=1
        kaburi = 0
        plus = 0
        for j in range(T):
            if i==j:
                continue
            kaburi+=(pat[i][j]*teams[j][0])%mod
            plus += bigpower(N,F-1-free)*teams[j][0]%mod
            kaburi%=mod
            plus%=mod
            ans%=mod
            pat[j][i]+=(pat[i][j]*teams[j][0])%mod
            pat[j][i]%=mod
            pat[i][j]=pat[j][i]
        ans-=((plus-kaburi)*bigpower(N,free))%mod
        ans%=mod
print(ans)