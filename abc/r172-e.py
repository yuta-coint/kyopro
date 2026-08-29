Q = int(input())
#1の位から合わせていけばよい
d1 = [pow(i,i,10) for i in range(20)]
for case in range(Q):
    X=int(input())
    cand = set()
    if X ==1:
        print(1)
        continue
    #mod 20での解
    for i in range(20):
        if d1[i]==X%10:
            cand.add(i)
    for i in range(2,10):
        newcand = set()
        for c in cand:
            for j in range(10):
                nc = c+j*2*(10**(i-1))
                if pow(nc,nc,10**i) == X%(10**i):
                    newcand.add(nc)
        cand = newcand
    print(min(cand))