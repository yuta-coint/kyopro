import sys
input = sys.stdin.readline
sys.setrecursionlimit(30000)
n,x=map(int,input().split())
a = []
for i in range(n):
    la = list(map(int,input().split()))
    l = la[0]
    ai = la[1:]
    a.append(ai)
def search(pro,k):
    if k==n:
        if pro==x:
            return(1)
        else:
            return(0)
    else:
        cnt = 0
        for ball in a[k]:
            cnt+=search(pro*ball,k+1)
        return(cnt)
print(search(1,0))
