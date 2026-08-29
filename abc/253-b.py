H,W = map(int,input().split())
t = 0
for i in range(H):
    s = input()
    for j in range(W):
        if s[j]=="o":
            if t==0:
                x1=i
                y1=j
                t=1
            else:
                x2=i
                y2=j
print(abs(x1-x2)+abs(y1-y2))
