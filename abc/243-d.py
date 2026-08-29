import sys
input = sys.stdin.readline
n,x = map(int,input().split())
s= input()
depth = len(bin(x))-2
for i in range(n):
    if s[i]=="U":
        depth-=1
    else:
        depth+=1
    if depth >61:
        continue
    if depth==61 and s[i]=="U":
        continue
    if s[i]=="U":
        x//=2
    elif s[i]=="L":
        x*=2
    else:
        x*=2
        x+=1
print(x)