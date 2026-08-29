ans = []
N = 62
ans.append(("+",0,1,3))
ans.append(("<",4,3,3))
#3からN+3まで埋める。
for i in range(N):
    ans.append(("+",3 + i, 3 + i, 3 + i + 1))
#N+4から2N+3まで埋める。
start = N + 4
temp = N*N + 4 * N + 8
ans.append(("+",0,3,temp))
for i in reversed(range(N)):
    ans.append(("+",2 * N + 4, 3 + i, 2 * N + 5))
    ans.append(("<",2 * N + 5, temp, start + i))
    for j in range(i):
        ans.append(("+", start + i, start + i, start + i))
    ans.append(("+",start + i, 2 * N + 4, 2 * N + 4))
#同様に、2N+6から3N+5まで埋める。
start = 2 * N + 6
ans.append(("+",1,3,temp))
for i in reversed(range(N)):
    ans.append(("+",3 * N + 6, 3 + i, 3 * N + 7))
    ans.append(("<",3 * N + 7, temp, start + i))
    for j in range(i):
        ans.append(("+", start + i, start + i, start + i))
    ans.append(("+",start + i, 3 * N + 6, 3 * N + 6))
#最後に、N*N個の要素について処理を行う。
temp = N*N + 4 * N + 7
temp3 = N*N + 4 * N + 9
for i in range(N):
    for j in range(N):
        #N + 4 + iと2 * N + 6 + jについて調べて、結果を、3 * N + 6 + N * i + jに入れる。
        temp2 = 3 * N + 6 + N * i + j
        ans.append(("+", 3 + i, 3 + j, temp))
        ans.append(("+", N + 4 + i, 2 * N + 6 + j, temp2))
        ans.append(("+", temp2, 3, temp2))
        ans.append(("<", temp, temp2, temp2))
        ans.append(("+", temp2, temp3 + i + j, temp3 + i + j))
for i in range(N):
    for j in range(i):
        ans.append(("+", temp3 + i, temp3 + i, temp3 + i))
    ans.append(("+", 2, temp3 + i, 2))
print(len(ans))
A = [0 for i in range(10**6)]
x,y = map(int,input().split())
A[0] = x
A[1] = y
for i in range(len(ans)):
    cmd,a,b,c = ans[i]
    if cmd == "+":
        A[c] = A[a] + A[b]
    else:
        if A[a] < A[b]:
            A[c] = 1
        else:
            A[c] = 0
    print(*ans[i])
print(A[2])