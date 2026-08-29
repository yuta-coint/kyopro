from copy import copy
N = int(input())
A = list(map(int,input().split()))
ans = set()
#range(N)の分割を全て列挙
Q = [([],0,0)]
while Q:
    S,d,r = Q.pop()
    if d==N:
        #set_partition.append(copy(R))
        #ここから各分割についての処理を書く
        temp = [0 for i in range(N)]
        for i in range(N):
            temp[S[i]]+=A[i]
        hoge = 0
        for i in range(N):
            hoge^=temp[i]
        ans.add(hoge)
        #ここまで
    else:
        R = copy(S)
        for i in range(r+1):
            if i==0:
                R.append(i)
            else:
                R[d]=i
            if i<r:
                Q.append((copy(R),d+1,r))
            else:
                Q.append((copy(R),d+1,r+1))
            #print(R)
#print(set_partition)
print(len(ans))