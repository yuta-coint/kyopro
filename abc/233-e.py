x = list(input())
for i in range(len(x)):
    x[i] = int(x[i])
for i in range(1,len(x)):
    x[i]+=x[i-1]
for i in reversed(range(1,len(x))):
    x[i-1] += x[i]//10
    x[i]%=10
print(*x,sep="")