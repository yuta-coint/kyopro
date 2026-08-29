N = int(input())
A = list(map(int,input().split()))
from collections import defaultdict
contena = [defaultdict(int) for i in range(9)]
for i in range(N):
    for keta in range(9):
        