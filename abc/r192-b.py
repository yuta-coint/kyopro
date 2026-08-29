N=  int(input())
A = list(map(int,input().split()))
odd = 0
even = 0
for i in range(N):
    if A[i]%2==0:
        even+=1
    else:
        odd+=1
if odd<=2 and even<=2:
    if (odd+even)%2==0:
        print("Snuke")
    else:
        print("Fennec")
else:
    if odd%2==0:
        print("Snuke")
    else:
        print("Fennec")

ans = [[[0 for k in range(2)] for j in range(20)] for i in range(20)]
for i in range(20):
    for j in range(20):
        if i==0 and j==0:
            continue
        for k in range(2):
            temp = []
            if i>=1:
                temp.append(ans[i-1][j][k])
            if j>=1:
                temp.append(ans[i][j-1][k^1])
            if k==1:
                temp.append(ans[i][j][0])
            for s in range(4):
                if not (s in temp):
                    ans[i][k][k] = s
                    break
for i in range(20):
    print(ans[i])