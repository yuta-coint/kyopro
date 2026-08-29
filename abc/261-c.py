N = int(input())
d = {}
for i in range(N):
    S = input()
    if S in d:
        d[S]+=1
        print(S+"("+str(d[S])+")")
    else:
        d[S]=0
        print(S)