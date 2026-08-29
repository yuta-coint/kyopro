n =  int(input())
a = list(map(int,input().split()))
ans = 1
last  =-1
t = 1
m = 0
M = 10**5
while m+1<M:
    ans = (m+M)//2
    now = {}
    flag = False
    for i in range(n):
        if last==a[i]:
            now[a[i]][0]+=1
        elif last<a[i]:
            now[a[i]]=[0,t]
        else:
            t+=1
            now[a[i]][0]+=1
        k = a[i]
        while True:
            #繰り上がり
            if now[k][0]==ans:
                k-=1
                if now[k][1]==t:
                    now[k][0]+=1
                else:
                    now[k]=[0,t]
            else:
                break
            if k==-1:
                flag = True
                break
    if flag:
        M = ans
    else:
        m=ans
print(m)