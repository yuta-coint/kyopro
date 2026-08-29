def main():
    N = int(input())
    A =  [list(input()) for i in range(N)]
    ans = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i==0 and j==0:
                continue
            for x in range(N):
                for y in range(N):
                    temp = ""
                    s=x
                    t=y
                    for p in range(N):
                        temp+=A[s][t]
                        t+=i
                        t%=N
                        s+=j
                        s%=N
                    ans=max(ans,int(temp))
    print(ans)
main()