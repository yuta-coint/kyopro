import sys
input = sys.stdin.readline
N = int(input())
out = []
big = 10**6
d = {}
cnt = 1
for i in range(12):
    for l in range(1,4001):
        if l+(1<<i)<=N+1:
            out.append((l,l+(1<<i)-1))
            d[l*big+l+(1<<i)]=cnt
            cnt+=1
print(len(out))
for i in out:
    print(i[0],i[1])
sys.stdout.flush()
Q = int(input())
for _ in range(Q):
    L,R = map(int,input().split())
    t = len(bin(R+1-L))-3
    #print(t)
    t1,t2 = L*big+L+(1<<t),(R+1-(1<<t))*big+R+1
    print(d[t1],d[t2])
    sys.stdout.flush()
