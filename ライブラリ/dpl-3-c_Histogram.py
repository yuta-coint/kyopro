n = int(input())
h = list(map(int,input().split()))
SIS = [(-1,-1)]
#h[i]を天井とする長方形を考える
#左側の衝突地点を考える。既出のもので高さがaより下でかつ、最も右にあるものを考える。左上にある者の存在は抹消される
left_limit = []
for i in range(n):
    a = h[i]
    while SIS[-1][0]>=a:
        SIS.pop()
    left_limit.append(SIS[-1][1]+1)
    SIS.append((a,i))
SIS = [(-1,-1)]
right_limit = []
for i in range(n):
    a = h[n-1-i]
    while SIS[-1][0]>=a:
        SIS.pop()
    right_limit.append(n-SIS[-1][1]-1)
    SIS.append((a,i))
ans = 0
#print(left_limit)
#print(right_limit)
for i in range(n):
    ans = max(ans,(right_limit[n-1-i]-left_limit[i])*h[i])
print(ans)