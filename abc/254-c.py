def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    ls = [[] for i in range(K)]
    for i in range(N):
        ls[i%K].append(a[i])
    for i in range(K):
        ls[i].sort()
    ma = 0
    for i in range(N):
        if ls[i%K][i//K]>=ma:
            ma = ls[i%K][i//K]
        else:
            print("No")
            break
    else:
        print("Yes")
main()