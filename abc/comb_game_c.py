#Alice…D においてつぶす、Cにおいて確保
T = int(input())
for _ in range(T):
    A,B,C,D = map(int,input().split())
    score_Alice = 2 * B
    score_Bob = 2 * A
    if C > D:
        score_Bob += ((C-D)//2)
    else:
        score_Alice += ((D-C + 1)//2)
    if score_Alice > score_Bob:
        print("Alice")
    else:
        print("Bob")
