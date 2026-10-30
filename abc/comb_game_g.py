T = int(input())
for _ in range(T):
    #決着が早い山以外で遅延行為を続ければよい
    N = int(input())
    turns = 10**24
    for i in range(N):
        a,b = map(int,input().split())
        if a % (b + 1) == 0:
            tmp = (a//(b + 1)) * 2
        else:
            tmp = (a//(b + 1)) * 2 + 1
        if tmp < turns:
            turns = tmp
    if turns&1:
        print("Alice")
    else:
        print("Bob")