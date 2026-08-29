import bisect
n = int(input())
A = list(map(int,input().split()))
cnt = 0
ans1 = []
LIS = [-1]
for i in range(n):
    a = A[i]
    if a > LIS[-1]:
        LIS.append(a)
        cnt+=1
    else:
        LIS[bisect.bisect_left(LIS, a)] = a
    if a==LIS[-1]:
        ans1.append(cnt)
    else:
        ans1.append(0)
cnt = 0
ans2 = []
LIS = [-1]
for i in reversed(range(n)):
    a = A[i]
    if a > LIS[-1]:
        LIS.append(a)
        cnt+=1
    else:
        LIS[bisect.bisect_left(LIS, a)] = a
    if a==LIS[-1]:
        ans2.append(cnt)
    else:
        ans2.append(0)
ans = 0
#print(ans1)
#print(ans2)
for i in range(n):
    ans = max(ans1[i]+ans2[n-1-i]-1,ans)
print(ans)


