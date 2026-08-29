n = int(input())
a = list(map(int,input().split()))
#上の位が変わってから考えるやつ
S =[0 for i in range(10**6)]
T = [[0 for i in range(10**(6-j))] for j in range(6)]
for i in range(n):
    S[a[i]]+=1
plus = []
minus = []
for i in range(10**6):
    for j in reversed(range(6)):
        if i%(10**(6-j))-10**(5-j)>=0:
            S[i]+=T[j][i%(10**(6-j))-10**(5-j)]
        T[j][i%(10**(6-j))]=S[i]
ans = 0
#print(S[:100])
for i in range(n):
    ans += S[10**6-1-a[i]]
for i in range(n):
    for j in range(6):
        if a[i]%10>=5:
            break
        a[i]//=10
    else:
        ans-=1
print(ans//2)
    
    