N,Q = map(int,input().split())
S = list(input())
acc = [0]
cons = []
for i in range(N-1):
    if S[i]==S[i+1]:
        cons.append(1)
    else:
        cons.append(0)
for i in range(N-1):
    acc.append(acc[-1]+cons[i])
for i in range(Q):
    l,r = map(int,input().split())
    print(acc[r-1]-acc[l-1])