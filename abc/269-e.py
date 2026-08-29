import sys
N = int(input())
m=1
M=N+1
while m+1<M:
    temp=(m+M)//2
    print("?",1,N,m,temp-1)
    sys.stdout.flush()
    r = int(input())
    if r==temp-m:
        m=temp
    else:
        M=temp
ans1 = m
m=1
M=N+1
while m+1<M:
    temp=(m+M)//2
    print("?",m,temp-1,1,N)
    sys.stdout.flush()
    r = int(input())
    if r==temp-m:
        m=temp
    else:
        M=temp
ans2 = m
print("!",ans2,ans1)