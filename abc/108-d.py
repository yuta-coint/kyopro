n = int(input())
n-=1
e = len(bin(n+1))-3
ans = []
for i in range(e):
    ans.append([i+1,i+2,0])
    ans.append([i+1,i+2,2**i])
t = n-2**e+1
a = 2**e
for i in range(e):
    if t&1:
        ans.append([i+1,e+1,a])
        a+=2**i
    t>>=1
print(e+1,len(ans))
for i in ans:
    print(*i)