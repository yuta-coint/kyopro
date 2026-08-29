S = input()
cnt = 0
stk = []
for i in range(len(S)):
    stk.append(S[i])
    cnt+=1
    if cnt>=3:
        if stk[cnt-1]=="C" and stk[cnt-2]=="B" and stk[cnt-3]=="A":
            for _ in range(3):
                stk.pop()
            cnt-=3
print(*stk,sep="")