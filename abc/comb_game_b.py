H,W,N = map(int,input().split())
max_R,max_C,min_R,min_C = 0,0,H,W
for i in range(N):
    R,C = map(int,input().split())
    max_R = max(R,max_R)
    min_R = min(R,min_R)
    max_C = max(C,max_C)
    min_C = min(C,min_C)
a,b,c,d = min_R - 1,min_C - 1,H - max_R,W-max_C
if a^b^c^d == 0:
    print("Bob")
else:
    print("Alice")