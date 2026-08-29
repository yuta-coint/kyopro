N  =int(input())
A = [0]+list(map(int,input().split()))
ans = [0 for i in range(2*N+2)]
for i in range(1,1+N):
    ans[i*2]=ans[A[i]]+1
    ans[i*2+1]=ans[A[i]]+1
for i in range(1,2*N+2):
    print(ans[i])
