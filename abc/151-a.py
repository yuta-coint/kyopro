N = int(input())
S = input()
T = input()
hs = 0
ht = 0
for i in range(N):
    if S[i]=="1":
        hs+=1
    if T[i]=="1":
        ht+=1
U = ["0" for i in range(N)]
if (hs-ht)&1:
    print(-1)
elif hs>ht:
    cnt=0
    for i in reversed(range(N)):
        if S[i]=="1" and T[i]=="0":
            U[i]="1"
            cnt+=2
            if cnt==hs-ht:
                break
    print(*U,sep="")
elif hs==ht:
    print(*U,sep="")
else:
    cnt=0
    for i in reversed(range(N)):
        if S[i]=="0" and T[i]=="1":
            U[i]="1"
            cnt+=2
            if cnt==ht-hs:
                break
    print(*U,sep="")