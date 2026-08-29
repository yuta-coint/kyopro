T=int(input())
for _ in range(T):
    N,A,B,X,Y,Z = map(int,input().split())
    if X*A<=Y and X*B<=Z:
        ans = X*N
    elif X*A<=Y:
        ans = (N//B)*Z+(N%B)*X
    elif X*B<=Z:
        ans = (N//A)*Y+(N%A)*X
    else:
        ans = float('inf')
        for p in range(10**5):
            if p*A>N:
                break
            temp = p*Y
            temp+=((N-p*A)//B)*Z
            temp+=((N-p*A)%B)*X
        ans = min(ans,temp)
        for p in range(10**5):
            if p*B>N:
                break
            temp = p*Z
            temp+=((N-p*B)//A)*Y
            temp+=((N-p*B)%A)*X
        ans = min(ans,temp)
    print(ans)




