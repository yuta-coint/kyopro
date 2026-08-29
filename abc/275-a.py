N = int(input())
H = list(map(int,input().split()))
H = [(H[i],i+1) for i in range(N)]
H.sort(reverse=True)
print(H[0][1])