from math import isqrt
T = int(input())
sqsq = 10**5
table = [0,1]

#こいつでsqsq*sqsqまでやっていける
table_sum = [0,1]
for i in range(2,sqsq+1):
    table.append(table_sum[isqrt(i)])
    table_sum.append(table_sum[-1]+table[-1])
for i in range(T):
    N = int(input())
    sqN =  isqrt(N)
    sqsqN = isqrt(sqN)
    ans = 0
    for i in range(sqsqN):
        ans += table_sum[i]*(2*i+1)
    ans += table_sum[sqsqN]*(sqN-sqsqN*sqsqN+1)
    print(ans)
