def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')
    N = int(input())
    tree = [i for i in range(N)]

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
    sx,sy,tx,ty = map(int,input().split())
    circles = []
    for i in range(N):
        x,y,r = map(int,input().split())
        circles.append((x,y,r))
    for i in range(N):
        xa,ya,ra = circles[i]
        for j in range(i+1,N):
            xb,yb,rb = circles[j]
            if (ra-rb)**2 <= (xa-xb)**2 + (ya-yb)**2 <= (ra+rb)**2:
                union(i,j)
    for i in range(N):
        x,y,r = circles[i]
        if (x-sx)**2+(y-sy)**2==r**2:
            s=i
        if (x-tx)**2+(y-ty)**2==r**2:
            t=i
    if find(s)==find(t):
        print("Yes")
    else:
        print("No")
main()