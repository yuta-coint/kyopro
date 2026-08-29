N = int(input())
A = list(map(int,input().split()))
A_ind = [(A[i],i) for i in range(2 * N)]
from copy import copy
B = list(sorted(A_ind))
#print(B)
color = [-1 for i in range(2 * N)]
for i in range(N):
    color[B[i][1]] = 1
#print(color)
#(色, id)
temp = [(0,-1)]
ans = ["." for i in range(2 * N)]
for i in range(2 * N):
    if temp[-1][0] == -color[i]:
        ans[temp.pop()[1]] = "("
        ans[i] = ")"
    else:
        temp.append((color[i],i))
print(*ans,sep="")
