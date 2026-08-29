import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def main():
    N,M,Q = map(int,input().split())
    M+=1
    #RSQ
    #n:数列の長さ
    BIT = [0 for i in range(M+1)]
    def add(i,x):
        while i<=M:
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

    queries = [list(map(int,input().split())) for i in range(Q)]
    q3 = [[] for i in range(N+1)]
    ans = [-1 for i in range(Q)]
    for t in reversed(range(Q)):
        if queries[t][0]==1:
            l,r,x = queries[t][1],queries[t][2],queries[t][3]
            add(l,x)
            add(r+1,-x)
        elif queries[t][0]==2:
            i,x = queries[t][1],queries[t][2]
            for tj in q3[i]:
                ans[tj[0]]=getSum(tj[1])+x-tj[2]
            q3[i]=[]
        else:
            i,j = queries[t][1],queries[t][2]
            q3[i].append((t,j,getSum(j)))
        #for i in range(1,M+1):
            #print(getSum(i))
    for i in range(N+1):
        for tj in q3[i]:
            ans[tj[0]]=getSum(tj[1])-tj[2]
    for i in range(Q):
        if ans[i]!=-1:
            print(ans[i])
main()