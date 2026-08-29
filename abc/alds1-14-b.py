#Tの中のPの位置を調べる
T = input()
P = input()
mod = 10**9+7
ph = 0
th = 0
pow = 77
letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
d = {letter[i]:i for i in range(62)}
lp = len(P)
lt = len(T)
if lp<=lt:
    for i in range(len(P)):
        ph*=pow
        ph+=d[P[i]]
        ph%=mod
        th*=pow
        th+=d[T[i]]
        th%=mod
    rightp = 1
    for i in range(len(P)):
        rightp*=pow
        rightp%=mod
    for i in range(len(T)-lp):
        if th == ph:
            print(i)
        th*=pow
        th-=rightp*d[T[i]]
        th+=d[T[i+lp]]
        th%=mod
    if th == ph:
        print(len(T)-lp)