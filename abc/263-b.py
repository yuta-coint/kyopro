N = int(input())
P = list(map(int,input().split()))
ans = [0 for i in range(N)]
for i in range(1,N):
    ans[i] = ans[P[i-1]-1]+1
print(ans[-1])