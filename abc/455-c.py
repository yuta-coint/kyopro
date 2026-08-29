from collections import Counter
N, K = map(int,input().split())
A = list(map(int,input().split()))
count = Counter(A)
mult = []
for k in count.keys():
    mult.append(k * count[k])
mult.sort()
for i in range(min(len(mult),K)):
    mult.pop()
print(sum(mult))
