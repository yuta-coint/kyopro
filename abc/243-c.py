from ipaddress import ip_address
import sys
input = sys.stdin.readline
n = int(input())
md = {}
Md = {}
xy = [list(map(int,input().split())) for i in range(n)]
s = input()
for i in range(n):
    x,y = xy[i][0],xy[i][1]
    if s[i]=="L":
        if y in Md:
            Md[y]=max(Md[y],x)
        else:
            Md[y]=x
    else:
        if y in md:
            md[y]=min(md[y],x)
        else:
            md[y]=x
ans = "No"
for k in Md:
    if k in md:
        if Md[k]>md[k]:
            ans = "Yes"
print(ans)
