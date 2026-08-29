def main():
    import sys
    input = sys.stdin.readline
    N,M,E = map(int,input().split())
    n = N+1
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
    wire=[]
    for i in range(E):
        u,v = map(int,input().split())
        if u>N:
            u=0
        if v>N:
            v=0
        wire.append((u,v))
    Q = int(input())
    cut = [int(input()) for i in range(Q)]
    s_cut = set(cut)
    for i in range(E):
        if not (1+i in s_cut):
            union(wire[i][0],wire[i][1])
    ans = []
    ans.append(size[find(0)]-1)
    for i in reversed(range(1,Q)):
        #if wire[cut[i]-1][0]+wire[cut[i]-1][1]!=0:
        union(wire[cut[i]-1][0],wire[cut[i]-1][1])
        ans.append(size[find(0)]-1)
    for i in reversed(range(Q)):
        print(ans[i])
main()