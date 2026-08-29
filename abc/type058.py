N,K = map(int,input().split())
s = set([N])
loop = [N]
cnt = 0
while True:
    cnt+=1
    b = str(N)
    for i in range(len(b)):
        N+=int(b[i])
    N%=10**5
    if N in s:
        break
    else:
        loop.append(N)
        s.add(N)
t = loop.index(N)
if K<cnt:
    print(loop[K])
else:
    print(loop[(K-t)%(cnt-t)+t])