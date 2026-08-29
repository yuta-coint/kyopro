M = int(input())
D = [0]+list(map(int,input().split()))
day = []
for i in range(1,M+1):
    for j in range(D[i]):
        day.append((i,j+1))
L = len(day)
print(*day[(L-1)//2])