T = int(input())
for case in range(T):
    N,M = map(int,input().split())
    #ボブが最後に残したいカード
    if 0<N*(N+1)%M<=N:
        print("Bob")
    else:
        print("Alice")