N = int(input())
h = list(map(int,input().split()))
cost = [0]
cost.append(abs(h[0]-h[1]))
for i in range(2,N):
    cost.append(min(abs(h[i]-h[i-1])+cost[i-1],abs(h[i],h[i-2])+cost[i-2]))
print(cost[N-1])