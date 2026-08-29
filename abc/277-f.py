import sys
input = sys.stdin.readline
from typing import List
from collections import deque

def toposort(g: List[List[int]]) -> bool:
    # トポロジカルソートの可否を返す
    cnt = [0] * len(g)
    for frm in range(len(g)):
        for to in g[frm]:
            cnt[to] += 1
 
    q: deque = deque()
 
    for i, c in enumerate(cnt):
        if c == 0:
            q.append(i)
 
    while q:
        u = q.pop()
        for v in g[u]:
            cnt[v] -= 1
            if cnt[v] == 0:
                q.append(v)
 
    for c in cnt:
        if c != 0:
            return False
 
    return True

def main():
    H,W = map(int,input().split())
    #if H>10**5:
    #    return(0)
    A = [list(map(int,input().split())) for i in range(H)]
    #行で並び替えられますか?
    mami = []
    for i in range(H):
        sAi = set(A[i])
        sAi.discard(0)
        if sAi:
            pass
        else:
            continue
        B = sorted(sAi)
        mami.append((B[0],B[-1]))
    mami.sort()
    temp = -1
    for i in range(len(mami)):
        if temp>mami[i][0]:
            print("No")
            exit()
        temp = mami[i][1]
    #とぽろじかるそーと
    HW = [[] for i in range(1+H*W+W)]
    for i in range(H):
        Ai = A[i]
        sAi = set(Ai)
        sAi.discard(0)
        if sAi:
            pass
        else:
            continue
        ssa =  sorted(sAi)
        if ssa[0]==ssa[-1]:
            continue
        next = {ssa[j]:ssa[j+1] for j in range(len(ssa)-1)}
        for j in range(W):
            if Ai[j]==0:
                continue
            if Ai[j]!=ssa[0]:
                HW[Ai[j]].append(H*W+1+j)
            if Ai[j] in next:
                HW[H*W+1+j].append(next[Ai[j]])
    #print(HW)
    if toposort(HW):
        print("Yes")
    else:
        print("No")
main()