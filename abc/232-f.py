n,x,y= map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = [float('inf') for i in range(1<<n)]
ans[0]=0
popcount = [-1 for i in range(1<<n)]
for i in range(1<<n):
    for j in range(n):
        if (i>>j)&1:
            popcount[i]+=1
for circumstance in range(1,1<<n):
    for new in range(n):
        if (circumstance>>new)&1:
            inversion = 0
            for old in range(new+1,n):
                if (circumstance>>old)&1:
                    inversion+=1
            #print(i,ans[circumstance-(1<<new)],inversion)
            temp=ans[circumstance-(1<<new)]+abs(b[popcount[circumstance]]-a[new])*x+inversion*y
            if ans[circumstance]>temp:
                ans[circumstance]=temp
#print(ans)
print(ans[(1<<n)-1])

