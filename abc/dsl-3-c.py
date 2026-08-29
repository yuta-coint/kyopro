def main():
    N,Q = map(int,input().split())
    a = list(map(int,input().split()))
    X = list(map(int,input().split()))
    for x in X:
        window = 0
        l = 0
        ans = 0
        for r in range(N):
            window+=a[r]
            while window>x:
                window-=a[l]
                l+=1
            ans+=r-l+1
        print(ans)
main()