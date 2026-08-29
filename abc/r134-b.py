n = int(input())
s = list(input())
s = [ord(s[i])-ord("a") for i in range(n)]
cnt = [0 for i in range(26)]
for i in range(n):
    cnt[s[i]]+=1
now = 0
m = 0
M=n-1
d = [0 for i in range(26)]
for i in range(26):
    while d[i]<cnt[i] and m<M:
        if s[m]==i:
            d[s[m]]+=1
            m+=1
            continue
        if s[M]!=i:
            d[s[M]]+=1
            M-=1
            continue
        s[m],s[M]=s[M],s[m]
        d[s[M]]+=1
        M-=1
        d[s[m]]+=1
        m+=1
alpha = "abcdefghijklmnopqrstuvwxyz"
ans = [alpha[s[i]] for i in range(n)]
print(*ans,sep="")