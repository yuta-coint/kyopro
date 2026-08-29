from operator import itemgetter
from itertools import *
from bisect import *
from collections import *
from heapq import *
import sys
sys.setrecursionlimit(10**6)


tree = []
def find(i):
    if tree[i] == i:
        return i
    else:
        tree[i]= find(tree[i])
        return find(tree[i])

def union(a,b):
    global conn_comp
    if tree[a] > tree[b]:
        a,b = b,a
    tree[find(b)] = find(a)

mod = 998244353
T=int(input())
for _ in range(T):
    H,W = map(int,input().split())
    S = [input() for i in range(H)]
    ans = 0
    ctd = False
    yoko = [[0 for j in range(W)] for i in range(H)]
    tate = [[0 for j in range(W)] for i in range(H)]
    for i in range(H):
        for j in range(1,W):
            if S[i][j-1]=="A":
                yoko[i][j] = 1-yoko[i][j-1]
            else:
                yoko[i][j] = yoko[i][j-1]
        if S[i][W-1]=="A":
            if yoko[i][0]==yoko[i][W-1]:
                ctd=True
        else:
            if yoko[i][0]!=yoko[i][W-1]:
                ctd=True
    for j in range(W):
        for i in range(1,H):
            if S[i-1][j]=="A":
                tate[i][j] = 1-tate[i-1][j]
            else:
                tate[i][j] = tate[i-1][j]
        if S[H-1][j]=="A":
            if tate[0][j]==tate[H-1][j]:
                ctd=True
        else:
            if tate[0][j]!=tate[H-1][j]:
                ctd=True
    if ctd:
        print(0)
        continue
    tree = [i for i in range(H+W)]
    jiyudo = H+W
    G = [[] for i in range(H+W)]
    for i in range(H):
        for j in range(W):
            if S[i][j]=="A":
                continue
            if find(i)!=find(H+j):
                jiyudo-=1
                union(i,H+j)
            G[i].append(H+j)
            G[H+j].append(i)
    parent = [-1 for i in range(H+W)]
    color = [-1 for i in range(H+W)]
    done = [0] * (H*W)
    DT = []
    for p in range(H+W):
        if done[p]!=0:
            continue
        Q = [p] # 根をスタックに追加
        while Q:
            i = Q.pop()
            if done[i]==1:
                continue
            done[i] = 1
            DT.append(i)
            for a in G[i]:
                if done[a]: continue
                parent[a]=i
                Q.append(a) # 普通のdfsのときはこっち
    for f in DT:
        if parent[f]==-1:
            color[f] = 0
        else:
            if f>=H:
                if tate[parent[f]][f-H]^yoko[parent[f]][f-H]==1:
                    color[f] = 1-color[parent[f]]
                else:
                    color[f] = color[parent[f]]
            else:
                if tate[f][parent[f]-H]^yoko[f][parent[f]-H]==1:
                    color[f] = 1-color[parent[f]]
                else:
                    color[f] = color[parent[f]]
    for i in range(H):
        for j in range(W):
            if S[i][j]=="A":
                continue
            if tate[i][j]^yoko[i][j]^color[i]^color[H+j]==1:
                ctd = True
    if ctd:
        print(0)
    else:
        print(pow(2,jiyudo,mod))
            
    