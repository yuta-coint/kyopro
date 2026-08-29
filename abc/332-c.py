N,M = map(int,input().split())
S = input()
muji = M
logo = 0
ans = 0
for i in range(N):
    if S[i]=="0":
        muji = M
        logo = 0
    elif S[i]=="1":
        if muji>0:
            muji-=1
        else:
            logo-=1
            if -logo>ans:
                ans=-logo
    else:
        logo-=1
        if -logo>ans:
            ans = -logo
print(ans)