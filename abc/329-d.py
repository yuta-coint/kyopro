N,M=map(int,input().split())
A = list(map(int,input().split()))
champ = 1
score = [0 for i in range(N+1)]
for i in range(M):
    score[A[i]]+=1
    if score[A[i]]>score[champ]:
        print(A[i])
        champ = A[i]
    elif score[A[i]]<score[champ]:
        print(champ)
    elif A[i]<champ:
        print(A[i])
        champ = A[i]
    else:
        print(champ)