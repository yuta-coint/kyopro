import bisect
from itertools import product
import sys
input = sys.stdin.readline
def main():
    N,W = map(int,input().split())
    goods = [list(map(int,input().split())) for i in range(N)]
    g1 = goods[:N//2]
    v1 = [g[0] for g in g1]
    w1 = [g[1] for g in g1]
    g2 = goods[N//2:]
    v2 = [g[0] for g in g2]
    w2 = [g[1] for g in g2]
    b1 = []
    b2 = []
    for bits in product([0,1],repeat=N//2):
        values = [x for bit, x in zip(bits, v1) if bit == 1]
        weights = [x for bit, x in zip(bits, w1) if bit == 1]
        b1.append([sum(weights),sum(values)])
    for bits in product([0,1],repeat=(N+1)//2):
        values = [x for bit, x in zip(bits, v2) if bit == 1]
        weights = [x for bit, x in zip(bits, w2) if bit == 1]
        b2.append([sum(weights),sum(values)])
    b2.sort()
    w2 = [g[0] for g in b2]
    v2 = [g[1] for g in b2]
    for i in range(1,len(v2)):
        if v2[i]<v2[i-1]:
            v2[i]=v2[i-1]
    ans = 0
    #print(b1)
    #print(v2)
    #print(w2)
    for g in b1:
        if g[0] > W:
            continue
        temp = v2[bisect.bisect_right(w2,W-g[0])-1]+g[1]
        if ans<temp:
            ans=temp
    print(ans)
main()