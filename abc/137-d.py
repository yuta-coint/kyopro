N,M = map(int,input().split())
a = list(map(int,input().split()))
ans = [0 for i in range(M)]
mod = 2
for t in 30:
    temp = []
    for i in reversed(range(N)):
        temp.append((a[i]>>i)&1)
    for i in range(N):
        


    
    