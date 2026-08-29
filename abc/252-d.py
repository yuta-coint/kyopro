N = int(input())
A= list(map(int,input().split()))
T = max(A)
chk = [0 for i in range(T+1)]
for i in range(N):
    chk[A[i]]+=1
flag = 0
ans = 0
two = 0
for i in range(T+1):
    if chk[i]==0:
        continue
    if flag==0:
        flag+=1
        one=chk[i]
    elif flag == 1:
        two=one*chk[i]
        one+=chk[i]
        flag+=1
    else:
        ans+=two*chk[i]
        two+=one*chk[i]
        one+=chk[i]
print(ans)

