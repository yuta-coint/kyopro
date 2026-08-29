n,m=map(int,input().split())
s = list(input().split())
t = list(input().split())
d = {s[i]:i for i in range(n)}
chk = [False for i in range(n)]
for i in t:
    chk[d[i]]=True
for i in range(n):
    if chk[i]:
        print("Yes")
    else:
        print("No")