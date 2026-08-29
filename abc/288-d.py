from copy import copy
N,K = map(int,input().split())
A = list(map(int,input().split()))
temp = [0 for i in range(K)]
range_sum = [temp.copy()]
for i in range(N):
    temp[i%K]+=A[i]
    range_sum.append(temp.copy())
#print(range_sum)
Q = int(input())
for _ in range(Q):
    l,r = map(int,input().split())
    check = [range_sum[r][i]-range_sum[l-1][i] for i in range(K)]
    if K == 1:
        print("Yes")
    else:
        for i in range(K-1):
            if check[i]!=check[i+1]:
                print("No")
                break
        else:
            print("Yes")