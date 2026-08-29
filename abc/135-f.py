s = input()
t = input()
ls = len(s)
lt = len(t)
ss = s*(((ls+lt-2)//ls)+1)
T = ss[:ls+lt-1]
P = t
#文字列の検索結果を確認
find = [0 for i in range(ls)]
mod = 10**9+7
letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
d = {letter[i]:i for i in range(62)}
pow = 77
LP = len(P)
LT = len(T)
ph = 0
th = 0
if LP<=LT:
    for i in range(LP):
        ph*=pow
        ph+=d[P[i]]
        ph%=mod
        th*=pow
        th+=d[T[i]]
        th%=mod
    rightp = 1
    for i in range(LP):
        rightp*=pow
        rightp%=mod
    for i in range(LT-LP):
        if th == ph:
            find[i]=1
        th*=pow
        th-=rightp*d[T[i]]
        th+=d[T[i+LP]]
        th%=mod
    if th == ph:
        find[LT-LP]=1
check = [0 for i in range(ls)]
ans = 0
infi = 0
for start in range(LP):
    start%=ls
    if check[start]==2:
        continue
    k = start
    score = 0
    f = 1
    while check[k]<2:
        check[k]+=1
        k+=LP
        k%=ls
        if find[k]==1:
            score+=1
            ans = max(score,ans)
        else:
            score=0
            f = 0
    if f==1:
        infi = 1
if infi == 1:
    print(-1)
else:
    print(ans)
        
