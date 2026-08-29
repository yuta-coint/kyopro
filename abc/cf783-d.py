t = int(input())
import sys
input = sys.stdin.readline
from bisect import bisect
for _ in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    base = 0
    dp = []
    for i in range(n):
        base+=a[i]
        if a[i]<0:
            if bisect[a[i]]>0:
                


