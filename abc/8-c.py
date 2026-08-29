n = int(input())
mul = [0 for i in range(n)]
coin = [int(input()) for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        if coin[i]%coin[j]==0:
            mul[i]+=1
ans = [0 for i in range(n)]
half= 0
for i in mul:
    if i%2==1:
        half+=1
    else:
        ans[i]+=1
a = 0
for i in range(n):
    a+=(i//2+1)*ans[i]/(i+1)
a += half/2
print(a)