import sys
input = sys.stdin.readline
n,m = map(int,input().split())
tree = [i for i in range(n)]
size = [1 for i in range(n)]

def find(i):
    if tree[i] == i:
        return i
    else:
        tree[i]= find(tree[i])
        return find(tree[i])

def union(a,b):
    if tree[a] > tree[b]:
        a,b = b,a
    if find(a)!=find(b):
        size[find(a)],size[find(b)]=size[find(b)]+size[find(a)],size[find(b)]+size[find(a)]
    tree[find(b)] = find(a)

city = []
city = [list(map(lambda x:int(x)-1,input().split())) for i in range(m)]
q = int(input())
people = []
for i in range(q):
    v,w = map(lambda x:int(x)-1,input().split())
    people.append([w,v,i])
city.sort(reverse=True,key=lambda x: x[2])
people.sort(reverse=True)
counter=0
ans = [0 for i in range(q)]
for i in range(q):
    while True:
        if counter==m:
            break
        if city[counter][2]>people[i][0]:
            union(city[counter][0],city[counter][1])
            counter+=1
        else:
            break
    ans[people[i][2]]=size[find(people[i][1])]
for i in range(q):
    print(ans[i])


