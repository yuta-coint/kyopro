H,W = map(int,input().split())
A = [list(input()) for i in range(H)]
B = [list(input()) for i in range(H)]
for s in range(H):
    for t in range(W):
        if [[A[(i+s)%H][(j+t)%W] for j in range(W)] for i in range(H)]==B:
            print("Yes")
            exit()
print("No")