import sys
input = sys.stdin.readline
n,m = map(int,input().split())
rank = [0 for i in range(n+1)]
rank.append(-2**31)
edge = []
# N: 処理する区間の長さ
N=n+1
N0 = 2**(N-1).bit_length()
data = [None]*(2*N0)
INF = (-1, 2**31-1)
# 区間[l, r+1)の値をvに書き換える
# vは(t, value)という値にする (新しい値ほどtは大きくなる)
def update(l, r, v):
    L = l + N0; R = r + N0
    while L < R:
        if R & 1:
            R -= 1
            data[R-1] = v

        if L & 1:
            data[L-1] = v
            L += 1
        L >>= 1; R >>= 1
# a_iの現在の値を取得
def _query(k):
    k += N0-1
    s = INF
    while k >= 0:
        if data[k]:
            s = max(s, data[k])
        k = (k - 1) // 2
    return s
# これを呼び出す
def query(k):
    return _query(k)[1]

data2 = [None]*(2*N0)
# 区間[l, r+1)の値をvに書き換える
# vは(t, value)という値にする (新しい値ほどtは大きくなる)
def update2(l, r, v):
    L = l + N0; R = r + N0
    while L < R:
        if R & 1:
            R -= 1
            data2[R-1] = v

        if L & 1:
            data2[L-1] = v
            L += 1
        L >>= 1; R >>= 1
# a_iの現在の値を取得
def _query2(k):
    k += N0-1
    s = INF
    while k >= 0:
        if data2[k]:
            s = max(s, data2[k])
        k = (k - 1) // 2
    return s
# これを呼び出す
def query2(k):
    return _query2(k)[1]

for i in range(m):
    l,r = map(int,input().split())
    edge.append([l-1,r])
edge.sort()
rank[0]=0
t = 0
update(0,n+1,(t,0))
update2(0,n+1,(t,n+1))
for p in edge:
    l1 = query(p[0])
    r1 = query2(p[0])
    l2 = query(p[1])
    r2 = query2(p[1])
    print(rank[l1]-(p[0]-l1),rank[r1]-(r1-p[0]),rank[l2]-(p[1]-l2),rank[r2]-(r2-p[1]))
    dep = max(rank[l1]-(p[0]-l1),rank[r1]-(r1-p[0]),rank[l2]-(p[1]-l2),rank[r2]-(r2-p[1]))
    rank[p[0]]=dep
    rank[p[1]]=dep
    t+=1
    if p[0]<r1:
        update(p[0],r1-1,(t,p[0]))
    if p[1]<r2:
        update(p[1],r2-1,(t,p[1]))
    if l1<p[0]:
        update2(l1+1,p[0],(t,p[0]))
    if l2<p[1]:
        update2(l2+1,p[1],(t,p[1]))
print(rank)
for i in range(n+1):
    l1 = query(i)
    r1 = query2(i)
    rank[i] = max(rank[l1]-(i-l1),rank[r1]-(r1-i))
ans = ""
for i in range(n):
    if rank[i+1]-rank[i]==1:
        ans+="1"
    else:
        ans+="0"
print(ans)



