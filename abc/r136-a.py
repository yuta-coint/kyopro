import sys
input = sys.stdin.readline
n = int(input())
ans=[]
cnt = 0
s = input()
for i in range(n):
    if s[i]=="A":
        cnt+=2
    elif s[i]=="B":
        cnt+=1
    else:
        for _ in range(cnt//2):
            ans.append("A")
        if cnt%2==1:
            ans.append("B")
        ans.append("C")
        cnt=0
for _ in range(cnt//2):
    ans.append("A")
if cnt%2==1:
    ans.append("B")
print(*ans,sep="")
