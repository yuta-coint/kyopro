n = int(input())
a = list(map(int,input().split()))
ans=0
top = 0
time = 0
stk = [(0,0)]
for i in range(n):
    ans+=1
    if a[i]==stk[-1][0]:
        stk.append((a[i],stk[-1][1]+1))
        if a[i]==stk[-1][1]:
            for j in range(a[i]):
                stk.pop()
                ans-=1
    else:
        stk.append((a[i],1))
    print(ans)


