from collections import Counter
N = int(input())
S = input()
ans = N * (N + 1)//2
pairs = [("A","B"),("B","C"),("C","A")]
for p in range(3):
    a,b = pairs[p]
    c = [0 for i in range(N+1)]
    for i in range(N):
        if S[i] == a:
            c[i + 1] = c[i] + 1
        elif S[i] == b:
            c[i + 1] = c[i] - 1
        else:
            c[i + 1] = c[i]
    if p == 0:
        c0 = c
    elif p == 1:
        c1 = c
    count = Counter(c)
    for k in count.keys():
        ans -= count[k] * (count[k] - 1)//2
#全部一致しているやつの2倍を足す。 
c = [c0[i]*(10**6) + c1[i] for i in range(N + 1)]
count = Counter(c)
for k in count.keys():
    ans += count[k] * (count[k] - 1)
print(ans)