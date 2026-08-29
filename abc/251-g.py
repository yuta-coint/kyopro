import sys
input = sys.stdin.readline
#2点のベクトルを求める
def vec(a, b):
    return (a[0] - b[0], a[1] - b[1])

N = int(input())
poly = [tuple(map(int,input().split())) for i in range(N)]
poly.append(poly[0])
M= int(input())
check = []
boarder = []
dif = [tuple(map(int,input().split())) for i in range(M)]
for i in range(N):
    x,y = vec(poly[i+1],poly[i])
    check.append((-y,x))
    b = -10**24
    for u,v in dif:
        if -y*(u+poly[i][0])+x*(v+poly[i][1])>b:
            b = -y*(u+poly[i][0])+x*(v+poly[i][1])
    boarder.append(b)
#print(poly)
#print(dif)
#print(check)
#print(boarder))
Q = int(input())
for _ in range(Q):
    a,b = map(int,input().split())
    for i in range(N):
        if check[i][0]*a+check[i][1]*b<boarder[i]:
            print("No")
            break
    else:
        print("Yes")