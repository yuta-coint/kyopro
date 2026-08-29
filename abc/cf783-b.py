t = int(input())
import sys
input = sys.stdin.readline
for i in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    need = sum(a)+max(a)-min(a)+n
    if need<=m:
        print("YES")
    else:
        print("NO")

