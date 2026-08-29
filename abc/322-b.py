N,M = map(int,input().split())
S = input()
T = input()
ans = 3
if T[M-N:]==S:
    ans-=1
if T[:N]==S:
    ans-=2
print(ans)