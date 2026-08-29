n,h = map(int,input().split())
a,b,c,d,e = map(int,input().split())
ans = float("inf")
#iは食事を取る日数
for i in range(n+1):
    money = c*i
    hunger = e*(n-i)-h
    hunger -= d*i
    if hunger>=0:
        rich = hunger//(b-d)+1
        if rich>i:
            continue
        money += (a-c)*rich
    #print(money)
    if money<ans:
        ans = money
print(ans)
