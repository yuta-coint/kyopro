import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000000)
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')
def main():
    N,Q = map(int,input().split())
    from math import gcd
    #RMQ
    c = 1
    n = 1
    while c<N:
        c*=2
        n+=1
    SEG = [0 for i in range(2**n)]#n段のセグ木
    def update(i,a):
        i += 2**(n-1)
        SEG[i]=a
        while i>1:
            i //= 2
            SEG[i] = gcd(SEG[2*i],SEG[2*i+1])
    def find(s,t):
        k = 0
        s += 2**(n-1)
        t += 2**(n-1)
        while s<=t:
            if s%2==1:
                k = gcd(k,SEG[s])
                s//=2
                s+=1
            else:
                s//=2
            if t%2==0:
                k = gcd(k,SEG[t])
                t//=2
                t-=1
            else:
                t//=2
        return(k)
    SEG2 = [0 for i in range(2**n)]#n段のセグ木
    def update2(i,a):
        i += 2**(n-1)
        SEG2[i]=a
        while i>1:
            i //= 2
            SEG2[i] = gcd(SEG2[2*i],SEG2[2*i+1])
    def find2(s,t):
        k = 0
        s += 2**(n-1)
        t += 2**(n-1)
        while s<=t:
            if s%2==1:
                k = gcd(k,SEG2[s])
                s//=2
                s+=1
            else:
                s//=2
            if t%2==0:
                k = gcd(k,SEG2[t])
                t//=2
                t-=1
            else:
                t//=2
        return(k)
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    for i in range(N-1):
        update(i,abs(A[i+1]-A[i]))
    for i in range(N-1):
        update2(i,abs(B[i+1]-B[i]))
    #print(SEG)
    #print(SEG2)
    #print(find(1,2))
    #print(find2(2,3))
    for i in range(Q):
        h1,h2,w1,w2 = map(int,input().split())
        ans = A[h1-1]+B[w1-1]
        if h1<h2:
            f = find(h1-1,h2-2)
            ans = gcd(ans,f)
        if w1<w2:
            f = find2(w1-1,w2-2)
            ans = gcd(ans,f)
        print(ans)
main()