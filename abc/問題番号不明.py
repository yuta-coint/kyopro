#r60-e
import sys
input = sys.stdin.readline
n = int(input())
E = list(map(int,input().split()))
L = int(input())
import math
l = math.ceil(math.log2(n))
Doubling = [[] for i in range(l)]
import bisect
for j in range(n):
    Doubling[0].append(bisect.bisect_right(E,E[j]+L)-1)
for i in range(1,l):
    for j in range(n):
        Doubling[i].append(Doubling[i-1][Doubling[i-1][j]])
#print(Doubling)
Q = int(input())
for i in range(Q):
    a,b = map(lambda x:int(x)-1,input().split())
    if a>b:
        a,b = b,a
    takahashi = a
    ans = 0
    for j in reversed(range(l)):
        if Doubling[j][takahashi]<b:
            takahashi = Doubling[j][takahashi]
            ans += 2**j
    if takahashi<b:
        ans+=1
    print(ans)
