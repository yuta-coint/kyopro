import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def main():
    #同じのを認めると座標圧縮に支障が出るので適当にずらす
    def rv(n,a):
        sa = sorted(a)
        #座標圧縮
        dict = {sa[i]:i+1 for i in range(n)}
        a = [dict[a[i]] for i in range(n)]
        #RSQ
        #n:数列の長さ
        BIT = [0 for i in range(n+1)]
        def add(i,x):
            while i<=n:
                BIT[i]+=x
                i += (i&-i)
        #xまでの和をとる
        def getSum(x):
            i = x
            gs = 0
            while i>0:
                gs+=BIT[i]
                i -= (i&-i)
            return gs
        ans = 0
        #同じ値を認めない場合、getSum(a[i]-1)になる
        for i in reversed(range(n)):
            ans+=getSum(a[i]-1)
            add(a[i],1)
        return(ans)
    N = int(input())
    X = list(map(int,input().split()))
    C = list(map(int,input().split()))
    temp = rv(N,C)
    L = [[] for i in range(N)]
    NN = [0 for i in range(N)]
    for i in range(N):
        L[X[i]-1].append(C[i])
        NN[X[i]-1]+=1
    for i in range(N):
        if NN[i]!=0:
            temp-=rv(NN[i],L[i])
            #print(L[i])
    print(temp)
main()

