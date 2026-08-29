N,M = map(int,input().split())
from itertools import permutations
S = [input() for i in range(N)]
for p in permutations(range(N)):
    for i in range(N-1):
        cnt = 0
        for j in range(M):
            if S[p[i]][j]!=S[p[i+1]][j]:
                cnt+=1
        if cnt!=1:
            break
    else:
        print("Yes")
        exit()
print("No")