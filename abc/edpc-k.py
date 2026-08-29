N,K = map(int,input().split())
a = list(map(int,input().split()))
win = [False for stone in range(K+1)]
for stone in range(K+1):
    for move in a:
        if stone<move:
            continue
        if win[stone-move]==False:
            win[stone]=True
            break
#print(win)
if win[K]:
    print("First")
else:
    print("Second")
