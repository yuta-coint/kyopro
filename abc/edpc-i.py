N = int(input())
p = list(map(float,input().split()))
#i回以上表が出る確率
head = [0 for i in range((N+3)//2)]
head[0]=1
for i in range(N):
    for j in reversed(range(1,(N+3)//2)):
        head[j]+=(head[j-1]-head[j])*p[i]
print(head[-1])