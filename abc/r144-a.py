N = int(input())
ans = []
if N%4>0:
    ans.append(N%4)
for i in range(N//4):
    ans.append(4)
print(N*2)
print(*ans,sep="")

