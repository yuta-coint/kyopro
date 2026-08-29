#1か0か自体はセグ木で更新していけば良くて、
#1とゼロで
N,Q = map(int,input().split())
S = input()
for _ in range(Q):
    c,L,R = map(int,input().split())
    