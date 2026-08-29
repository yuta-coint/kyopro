T = int(input())
import sys
input = sys.stdin.readline
for _ in range(T):
    N,M,K = map(int,input().split())
    S = list(input())
    cur = 0
    last = -2
    for i in range(N+M-3):
        if S[i]!=S[i+1]:
            if last==i-1:
                last = -2
            else:
                cur+=1
                last = i
    if cur<=K:
        print("Yes")
    else:
        print("No")
        