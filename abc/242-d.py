s = input()
q = int(input())
import sys
input = sys.stdin.readline
p = "ABC"
for i in range(q):
    t,k = map(int,input().split())
    k-=1
    if t>60:
        n=s[0]
    else:
        n=s[k//(1<<t)]
        k%=1<<t
    if n=="A":
        ans=0
    elif n=="B":
        ans =1
    else:
        ans = 2
    while k>0:
        ans+=k&1
        k>>=1
    ans%=3
    ans+=t
    ans%=3
    print(p[ans])
