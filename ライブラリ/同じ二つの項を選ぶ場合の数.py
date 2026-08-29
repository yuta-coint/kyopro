#同じ二つの項を選ぶ場合の数
a = []
a.sort()
ans = 0
pair=0
last = 0
cnt = 0
for i in a:
    if i==last:
        cnt+=1
    else:
        last= i
        ans+=cnt*(cnt-1)//2
        cnt=1
ans+=cnt*(cnt-1)//2