N,M,H,K = map(int,input().split())
S = list(input())
items = {}
big = 10**9
for i in range(M):
    x,y = map(int,input().split())
    items[big*x+y]=1
p,q = 0,0
for move in S:
    if move == "R":
        p+=1
    elif move == "L":
        p-=1
    elif move == "U":
        q+=1
    else:
        q-=1
    H-=1
    if H<0:
        print("No")
        exit()
    pq = p*big+q
    if pq in items:
        if items[pq]==1:
            if H<K:
                items[pq]=0
                H=K
print("Yes")