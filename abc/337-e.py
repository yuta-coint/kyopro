N = int(input())
import sys
M = len(bin(N-1))-2
print(M)
sys.stdout.flush()
for i in range(M):
    drink = []
    for j in range(N):
        if (j>>i)&1:
            drink.append(j+1)
    print([len(drink)]+drink)
    sys.stdout.flush()
ans = 1
S = input()
for i in range(M):
    if S[i]=="1":
        ans += 1<<i
print(ans)