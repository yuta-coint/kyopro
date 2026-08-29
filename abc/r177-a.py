kouka = [1,5,10,50,100,500]
coin = list(map(int,input().split()))
N = int(input())
X = list(map(int,input().split()))
for i in range(N):
    for k in reversed(range(6)):
        #使いたいもの
        need = X[i]//kouka[k]
        if need<=coin[k]:
            coin[k]-=need
            X[i]-=need*kouka[k]
        else:
            X[i]-=coin[k]*kouka[k]
            coin[k]=0
    if X[i]>0:
        print("No")
        exit()
print("Yes")