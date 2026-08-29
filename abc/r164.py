import sys
input = sys.stdin.readline
T = int(input())
for case in range(T):
    N,K = map(int,input().split())
    if N<K:
        print("No")
        continue
    mi = 0
    while N>0:
        mi+=N%3
        N//=3
    if K<mi:
        print("No")
        continue
    if (K-mi)&1:
        print("No")
    else:
        print("Yes")