T=  int(input())
for case in range(T):
    n,a,b = map(int,input().split())
    nb = ((a*n-a-b+1)//(b-a))+1
    