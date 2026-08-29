import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    waiting = [A[0]]
    L = 1
    ans = 0
    ca = [0 for i in range(15)]
    for i in range(N-1):
        tmp = False
        #まだA[i+1]が来ていない
        F = True
        while L > 1:
            if waiting[L-1] ==waiting[L-2]:
                waiting.pop()
                waiting[-1] += 1
                L -= 1
                ca[0] = 1
            elif waiting[L-1] >= A[i+1]:
                waiting.append(A[i+1])
                L += 1
                F = False
                ca[9] = 1
                break
            elif waiting[L-2] > A[i+1]:
                ans += A[i+1] - waiting[L-1]
                waiting[L-1] = A[i+1] + 1
                F = False
                ca[1]  =1
                break
            else:
                ans += waiting[L-2] - waiting[L-1]
                waiting.pop()
                L -= 1
                waiting[-1] += 1
                ca[3] = 1
        if F:
            if waiting[-1] <= A[i+1]:
                ans += A[i+1] - waiting[-1]
                waiting[-1] = A[i+1] + 1
                ca[4] = 1
            else:
                waiting.append(A[i+1])
                L += 1
                ca[5] = 1
        while L > 1:
            if waiting[L-2] == waiting[L-1]:
                waiting.pop()
                waiting[-1] += 1
                L -= 1
                ca[6] = 1
            else:
                ca[7] = 1
                break
    while L > 1:
        ans += waiting[L-2] - waiting[L-1]
        p = waiting.pop()
        waiting[-1] += 1
        L -= 1
    print(ans)
    print(ca)