import sys
input = sys.stdin.readline
N = int(input())
T = list(map(int,input().split()))
ans = 0
for i in range(N):
    t = 1<<T[i]
    ans=((ans+t)//(2*t))*(2*t)+t
print(ans)