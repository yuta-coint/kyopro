N,Q = map(int,input().split())
S = input()
rot = 0
for i in range(Q):
    t,x = map(int,input().split())
    if t==1:
        rot+=x
    else:
        print(S[(x-1-rot)%N])