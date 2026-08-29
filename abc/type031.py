Grundy = [[0 for j in range(1800)] for i in range(51)]
for j in range(51):
    for i in range(1500):
        check = [True for i in range(2000)]
        g = 0
        for k in range(1,(i//2)+1):
            check[Grundy[j][i-k]] = False
        if j>0:
            check[Grundy[j-1][i+j]] = False
        for k in range(1500):
            if check[k]:
                Grundy[j][i]=k
                break
N = int(input())
W = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 0
for i in range(N):
    ans^=Grundy[W[i]][B[i]]
if ans==0:
    print("Second")
else:
    print("First")