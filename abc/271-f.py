def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = [list(map(int,input().split())) for i in range(N)]
    k = [{} for i in range(N)]
    for bits in range(1<<(N-1)):
        i=0
        j=0
        temp = A[0][0]
        for b in range(N-1):
            if (bits>>b)&1:
                i+=1
            else:
                j+=1
            temp^=A[i][j]
        if temp in k[i]:
            k[i][temp]+=1
        else:
            k[i][temp]=1
    ans = 0
    for bits in range(1<<(N-1)):
        i=N-1
        j=N-1
        temp = A[i][j]
        for b in range(N-1):
            if (bits>>b)&1:
                i-=1
            else:
                j-=1
            temp^=A[i][j]
        temp^=A[i][j]
        if temp in k[i]:
            ans+=k[i][temp]
    print(ans)
main()
    
    