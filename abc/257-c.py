N  =int(input())
S = input()
W = list(map(int,input().split()))
temp = 0
for i in range(N):
    if S[i]=="1":
        W[i] = (W[i],0)
        temp+=1
    else:
        W[i] = (W[i],1)
W.sort()
ans=temp
for i in range(N):
    if W[i][1]==0:
        temp-=1
    else:
        temp+=1
    ans=max(temp,ans)
print(ans)