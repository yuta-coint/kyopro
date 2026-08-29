from itertools import combinations_with_replacement
cand = list(combinations_with_replacement(reversed(range(1,15)),3))
cand.sort()
ans = 0
N = int(input())
for t in cand[N-1]:
    ans += (10**t-1)//9
print(ans)