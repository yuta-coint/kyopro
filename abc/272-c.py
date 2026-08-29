N = int(input())
A = list(map(int,input().split()))
odd = []
even = []
for i in range(N):
    if A[i]&1:
        odd.append(A[i])
    else:
        even.append(A[i])
ans = -1
if len(odd)>=2:
    odd.sort(reverse=True)
    ans = max(odd[0]+odd[1],ans)
if len(even)>=2:
    even.sort(reverse=True)
    ans = max(even[0]+even[1],ans)
print(ans)