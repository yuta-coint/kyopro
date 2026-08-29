Q = int(input())
#受け取り方復習しよう！
from queue import Queue
mati = Queue()
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0]==1:
        mati.put(query[1])
    else:
        print(mati.get())