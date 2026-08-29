import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
h,w = map(int,input().split())
v = h*w
tree = [i for i in range(v)]

def find(i):
    if tree[i] == i:
        return i
    else:
        tree[i]= find(tree[i])
        return find(tree[i])

def union(a,b):
    if tree[a] > tree[b]:
        a,b = b,a
    tree[find(b)] = find(a)
tile = [0 for i in range(v)]
q = int(input())
for _ in range(q):
    q = list(map(int,input().split()))
    if q[0]==1:
        k = (q[1]-1)*w+(q[2]-1)
        tile[k]=1
        c = []
        if q[1]!=1:
            c.append(k-w)
        if q[1]!=h:
            c.append(k+w)
        if q[2]!=1:
            c.append(k-1)
        if q[2]!=w:
            c.append(k+1)
        for i in c:
            if tile[i]==1:
                union(i,k)
    else:
        k1 = (q[1]-1)*w+(q[2]-1)
        k2 = (q[3]-1)*w+(q[4]-1)
        if tile[k1]==1 and tile[k2] and find(k1)==find(k2):
            print("Yes")
        else:
            print("No")