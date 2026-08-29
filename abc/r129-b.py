import sys
input = sys.stdin.readline
n = int(input())
mir = 10**9
mal = 0
for i in range(n):
    l,r = map(int,input().split())
    if r<mir:
        mir=r
    if l>mal:
        mal=l
    if mir>=mal:
        print(0)
    else:
        print((mal-mir+1)//2)