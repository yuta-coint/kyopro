s = list(input())
mod = 998244353
pcq = [[1 for i in range(5001)]]
for i in range(1,5001):
    pcq.append([1])
    for j in range(1,5001):
        pcq[i].append((pcq[i][j-1]+pcq[i-1][j])%mod)
c = [0 for i in range(26)]
for i in s:
    c[ord(i)%26]+=1
a = [1]
cnt = 1
for ci in c:
    if ci ==0:
        continue
    cnt+=ci
    t = [0 for i in range(cnt)]
    for i in range(ci+1):
        for j in range(cnt-ci):
            t[j+i]+=(a[j]*pcq[j][i])%mod
            t[j+i]%=mod
    a = t
#print(a)
print((sum(a)-a[0])%mod)