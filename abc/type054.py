import sys
input = sys.stdin.readline
import queue
N,M = map(int,input().split())
author = [[] for i in range(N)]
journal = []
takahashi = [-1 for i in range(N)]
for i in range(M):
    K = int(input())
    R = list(map(lambda x:int(x)-1,input().split()))
    journal.append(R)
    for a in R:
        author[a].append(i)
j_checked = [False for i in range(M)]
a_checked = [False for i in range(N)]
q = queue.Queue()
q.put(0)
takahashi[0]=0
a_checked[0]=True
while not q.empty():
    v = q.get()
    for i in author[v]:
        #i…vが書いた論文
        if j_checked[i]:
            continue
        j_checked[i]=True
        for j in journal[i]:
            if a_checked[j]:
                continue
            takahashi[j]=takahashi[v]+1
            a_checked[j]=True
            q.put(j)
for i in range(N):
    print(takahashi[i])