N,M = map(int,input().split())
A = list(map(int,input().split()))
S = [list(input()) for i in range(N)]
scores = []
for i in range(N):
    sc = 0
    for q in range(M):
        if S[i][q]=="o":
            sc+=A[q]
    scores.append(sc+i+1)
top = max(scores)
pros = [(A[i],i) for i in range(M)]
pros.sort(reverse=True)
for i in range(N):
    temp = scores[i]
    ans = 0
    if temp==top:
        print(0)
        continue
    for q in range(M):
        if S[i][pros[q][1]]=="x":
            ans+=1
            temp+=pros[q][0]
            if temp>top:
                print(ans)
                break