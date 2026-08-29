N,A,B = map(int,input().split())
if A>B*2:
    A = B*2
ans = 0
S = list(input())
up = S.count("(")
down = S.count(")")
if up>down:
    #開き括弧が多すぎるので下から閉じ括弧にしていく
    cnt = 0
    ans += ((up-down)//2)*B
    for i in reversed(range(2*N)):
        if S[i]=="(":
            S[i]=")"
            cnt+=1
            if cnt==(up-down)//2:
                break
elif up<down:
    cnt = 0
    ans += ((down-up)//2)*B
    for i in range(2*N):
        if S[i]==")":
            S[i]="("
            cnt+=1
            if cnt==(down-up)//2:
                break
bott = 0
cur = 0
for i in range(2*N):
    if  S[i]=="(":
        cur+=1
    else:
        cur-=1
    if cur<bott:
        bott = cur
ans += (((-bott)+1)//2)*A
print(ans)