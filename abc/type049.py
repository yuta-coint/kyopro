import sys
input = sys.stdin.readline
def main():
    v,e = map(int,input().split())
    v+=1
    graph = []
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

    for i in range(e):
        w,s,t = map(int,input().split())
        s-=1
        graph.append([w,s,t])
    graph.sort()
    ans = 0
    for i in range(e):
        #print(tree)
        if find(graph[i][1])!=find(graph[i][2]):
            union(graph[i][1],graph[i][2])
            ans += graph[i][0]
        #print(ans)
    for i in range(1,v):
        if find(0)!=find(i):
            print(-1)
            break
    else:
        print(ans)
main()
