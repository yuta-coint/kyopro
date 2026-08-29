T = int(input())
for case in range(T):
    N = int(input())
    S = input()
    #BAがあるか
    ans = "A"
    for i in range(N):
        if S[i]=="B":
            ans = "B"
    for i in range(N-1):
        if S[i]=="B" and S[i+1]=="A":
            ans = "A"
    print(ans)