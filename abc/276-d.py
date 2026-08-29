N = int(input())
A = list(map(int,input().split()))
count_two = [0 for i in range(N)]
count_Three= [0 for i in range(N)]
for i in range(N):
    while A[i]%2==0:
        A[i]//=2
        count_two[i]+=1
    while A[i]%3==0:
        A[i]//=3
        count_Three[i]+=1
L = A[0]
for i in range(N):
    if A[i]!=A[0]:
        L=-1
        break
if L==-1:
    print(L)
else:
    print(sum(count_two)-min(count_two)*N+sum(count_Three)-min(count_Three)*N)