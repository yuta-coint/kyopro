N = int(input())
tank = 0
timer = 0
for i in range(N):
    T,V = map(int,input().split())
    tank = max(0,tank-(T-timer))
    timer  =T
    tank += V
print(tank)