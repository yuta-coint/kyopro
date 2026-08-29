N=  int(input())
ans = 0
logo = True
for i in range(N):
    S = input()
    if S=="login":
        logo = False
    elif S=="logout":
        logo = True
    elif S=="private":
        if logo:
            ans += 1
print(ans)