def main():
    N = int(input())
    X = list(input())
    X = ["0" for i in range(N-len(X))]+X
    X = [int(X[i]) for i in range(N)]
    cnt = 0
    def minus_one():
        dig = N
        for _ in range(N):
            dig-=1
            if X[dig]&1:
                break
            X[dig]=1
        else:
            return(0)
        X[dig]=0
        return(1)
    minus_one()
    ans = [1]
    for i in range(N):
        if X[i]==1:
            ans.append(1)
            X[i]=0
        else:
            if minus_one()==1:
                ans.append(0)
            else:
                break
    print(*ans,sep="")
main()