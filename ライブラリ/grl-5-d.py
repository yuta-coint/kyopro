#https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/5/GRL_5_D
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
nodes = [tuple(map(int,input().split())) for i in range(N)]
#Euler tourを作る
Euler  =[]
def EulerTour(n, X, i0):
    done = [0] * n
    Q = [-i0-1, i0] # 根をスタックに追加
    ET = []
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            ET.append(i)
            for j in range(1,1+X[i][0]):
                a = X[i][j]
                if done[a]: continue
                Q.append(~i) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加

        else: # 帰りがけの処理
            ET.append(-i-1)
    ET.pop()
    return ET
Euler = EulerTour(N,nodes,0)
len_Euler = len(Euler)
#print(Euler)
range_Euler = [[len_Euler+1,0] for i in range(N)]
for i in range(len_Euler):
    if range_Euler[Euler[i]][0]>i:
        range_Euler[Euler[i]][0]=i
    if range_Euler[Euler[i]][1]<i:
        range_Euler[Euler[i]][1]=i
#print(range_Euler)
#セグ木を作る
#RSQ
n=len_Euler
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

def RQT_add(u,w):
    add(range_Euler[u][0],w)
    add(range_Euler[u][1]+1,-w)
def RQT_getSum(u):
    return(getSum(range_Euler[u][0]))
q = int(input())
for _ in range(q):
    query =tuple(map(int,input().split()))
    if query[0]==0:
        RQT_add(query[1],query[2])
    else:
        print(RQT_getSum(query[1]))
    #print([RQT_getSum(i) for i in range(1,N)])