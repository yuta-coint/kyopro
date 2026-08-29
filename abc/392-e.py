import sys
input = sys.stdin.readline
n,m = map(int,input().split())
tree = [i for i in range(n)]
size = [1 for i in range(n)]
sys.setrecursionlimit(10**7)
conn_comp = n
def find(i):
    if tree[i] == i:
        return i
    else:
        tree[i]= find(tree[i])
        return find(tree[i])
def union(a,b):
    global conn_comp
    if tree[a] > tree[b]:
        a,b = b,a
    if find(a)!=find(b):
        conn_comp -= 1
    tree[find(b)] = find(a)
cut = []
for i in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    if find(a)==find(b):
        cut.append((a,i))
    union(a,b)
conn_cnt = [-1 for i in range(n)]
for a in range(n):
    conn_cnt[find(a)]=0
cut_class = [[] for _ in range(n)]
for a,i in cut:
    conn_cnt[find(a)]+=1
    cut_class[find(a)].append((i,a))
conn_cnt = [(conn_cnt[j],j) for j in range(n)]
conn_cnt.sort(reverse=True)
ans = []
key = 1
for t in range(n):
    if conn_cnt[t][0]==-1:
        break
    s,j = conn_cnt[t]
    for u,a in cut_class[j]:
        if key>=n:
            break
        ans.append((u+1,a+1,conn_cnt[key][1]+1))
        key+=1
hoge = 0
for i in range(n):
    hoge += len(cut_class[i])
#assert hoge<=n-1
print(conn_comp-1)
for i in range(conn_comp-1):
    print(*ans[i])