import sys
input = sys.stdin.readline
reset_time = -2
reset_num = 0
N = int(input())
A = list(map(int,input().split()))
A = [(A[i],-1) for i in range(N)]
Q = int(input())
for time in range(Q):
    query = tuple(map(int,input().split()))
    if query[0]==1:
        x = query[1]
        reset_time=time
        reset_num=x
    elif query[0]==2:
        i,x = query[1]-1,query[2]
        if reset_time>A[i][1]:
            A[i]=(x+reset_num,time)
        else:
            A[i]=(A[i][0]+x,time)
    else:
        i = query[1]-1
        if reset_time>A[i][1]:
            print(reset_num)
        else:
            print(A[i][0])