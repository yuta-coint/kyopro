N,X = map(int,input().split())
A = list(map(int,input().split()))
for score in range(101):
    B = A+[score]
    B.sort()
    if sum(B[1:N-1])>=X:
        print(score)
        exit()
print(-1)