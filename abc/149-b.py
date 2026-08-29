n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = [(A[i],B[i]) for i in range(n)]
C.sort()
B = [C[i][1] for i in range(n)]
import bisect
LIS = [-1]

for i in range(n):
    a = B[i]
    if a > LIS[-1]:
        LIS.append(a)
    else:
        LIS[bisect.bisect_left(LIS, a)] = a
print(len(LIS)-1+n)
