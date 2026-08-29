N,K = map(int,input().split())
med = [tuple(map(int,input().split())) for i in range(N)]
med.sort(reverse=True)
duty = 0
for a,b in med:
    duty+=b
    if duty>K:
        print(a+1)
        break
else:
    print(1)