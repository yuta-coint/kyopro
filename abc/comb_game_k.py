T = int(input())
for _ in range(T):
    A,B,C,D,E,F,G,H = map(int,input().split())
    Alice = 2 * B - 2 * A
    if H & 1:
        Alice += 1
    hand = H & 1
    if hand:
        Alice += G//2
    else:
        Alice += (G + 1)//2
    hand ^= (G & 1)
    if hand:
        Alice -= (F + 1)//2
    else:
        Alice -= F//2
    hand ^= (F & 1)
    hand ^= (E & 1)
    if hand:
        Alice += (D + 1)//2
    else:
        Alice += D//2
    hand ^= (D & 1)
    if hand:
        Alice -= C//2
    else:
        Alice -= (C + 1)//2
    hand ^= (C & 1)
    Alice += hand
    if Alice > 0:
        print("Alice")
    else:
        print("Bob")