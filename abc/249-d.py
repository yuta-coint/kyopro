def main():
    from math import floor
    N = int(input())
    A = list(map(int,input().split()))
    cnt = [0 for i in range(200001)]
    for i in A:
        cnt[i]+=1
    ans = 0
    for i in range(N):
        t = floor(A[i]**(1/2))
        for j in range(1,t+1):
            if A[i]%j!=0:
                continue
            if j*j==A[i]:
                ans+=cnt[j]*cnt[A[i]//j]
            else:
                ans+=cnt[j]*cnt[A[i]//j]*2
    print(ans)
main()

import sys

from regex import B
input=sys.stdin.readline
def main():
    N,K = map(int,input().split())
    S = [list(input()) for i in range(N)]
    ans = 0
    for i in range(2**N):
        cnt = [0 for _ in range(26)]
        for j in range(N):
            if (i>>j)&1:
                #print(i)
                continue
            s = S[j]
            #print(s)
            for k in range(len(s)-1):
                cnt[(ord(s[k])-ord("a"))%26]+=1
        #print(cnt)
        temp = 0
        for j in range(26):
            if cnt[j]==K:
                temp+=1
        ans = max(ans,temp)
    print(ans)
main()

small = False
large = False
s = input()
chk=set()
kabu = True
for i in range(len(s)):
    if 0<=ord(s[i])-ord("a")<=25:
        small = True
    if 0<=ord(s[i])-ord("A")<=25:
        large = True
    if ord(s[i])-ord("a") in chk:
        kabu = False
    chk.add(ord(s[i])-ord("a"))
if small and large and kabu:
    print("Yes")
else:
    print("No")

a,b,c,d,e,f,x = map(int,input().split())
takahasi = (x//(a+c))*+min(x%(a+c),a)*b
aoki = (x//(d+f))*e+min(x%(d+f),d)*e
if takahasi>aoki:
    print("Takahasi")
elif takahasi<aoki:
    print("Aoki")
else:
    print("Draw")
