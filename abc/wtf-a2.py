from collections import deque
T = int(input())
def reset():
    global conti,conti2,conti3
    global cnt,new_cnt
    global last
    global chkL,chkR
    ans.append(0)
    conti=0
    conti2=0
    conti3=0
    new_cnt = 0
    last="0"
    chkR = deque([])
    chkL = deque([])

for case in range(T):
    N = int(input())
    S = input()
    last = "0"
    conti = 0
    conti2 = 0
    conti3 = 0
    cnt=0
    new_cnt = 0
    chance = 0
    ans = []
    old_conti = deque([0 for i in range(1000)])
    chkR = deque()
    chkL = deque()
    for i in reversed(range(N)):
        if S[i]=="R":
            cnt+=1
            new_cnt+=1
            chkR.appendleft(i)
        else:
            cnt-=1
            new_cnt-=1
            chkL.appendleft(i)
        if S[i]==last:
            conti+=1
        else:
            conti3 = conti2
            conti2 = conti
            old_conti.appendleft(conti)
            conti=1
        if new_cnt*2==cnt:
            new_cnt = 10**9
        if new_cnt==0:
            reset()
            continue
        last = S[i]
        if S[i]=="R" and conti+1==old_conti[0] and cnt>=1:
            reset()
            continue
        if S[i]=="B" and conti+1==old_conti[0] and cnt<=-1:
            reset()
            continue
        if S[i]=="B" and conti==conti2 and conti3==1 and cnt>=1:
            ll = len(chkL)
            sana = 0
            for k in range(10000):
                if conti+k>=ll:
                    sana = k
                    break
                if chkL[conti+k]!=i+(2+k)*conti+-1+(k+2)*(k+1)//2:
                    sana = k
                    break
            print(sana,i)
            if sana&1:
                reset()
                continue
        if S[i]=="R" and conti==conti2 and conti3==1 and cnt<=-1:
            ll = len(chkR)
            sana = 0
            for k in range(10000):
                if conti+k>=ll:
                    sana = k
                    break
                if chkR[conti+k]!=i+(2+k)*conti+-1+(k+2)*(k+1)//2:
                    sana = k
                    break
            print(sana,i)
            if sana&1:
                reset()
                continue
        if cnt==0:
            reset()
        else:
            ans.append(1)
    ans.reverse()
    print(*ans,sep="")









N = int(input())
S = list(input())
a = input()
for i in range(N):
    if a[i]=="0":
        temp = 0
        for j in range(i,N):
            if a[j]==a[i]:
                temp+=1
            else:
                break
        for j in range(i,i+2*temp):
            S[j]="0"
print(S)