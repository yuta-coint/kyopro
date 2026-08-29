R,C = map(int,input().split())
c = max(abs(R-8),abs(C-8))
if c&1:
    print("black")
else:
    print("white")

