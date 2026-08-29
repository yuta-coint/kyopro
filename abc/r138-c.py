N = int(input())
a = list(map(int,input().split()))
b = [(a[i],i) for i in range(N)]
b.sort()
b = b[N//2:]
score = 0
for t in b:
    score += t[0]
    a[t[1]]=-1
for i in range(N):
    if a[i]>=0:
        a[i]=1
s = [a[0]]
mi=0
k=1
for i in range(1,N):
    s.append(s[-1]+a[i])
    if mi>s[-1]:
        mi = s[-1]
        k=i+1
print(k,score)
