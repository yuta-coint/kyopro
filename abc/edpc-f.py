s = input()
t = input()
ls = len(s)
lt = len(t)
#sのi文字目とtのj文字目があると困る
ans = [[0 for j in range(len(t)+1)]for i in range(len(s)+1)]
for i in range(1,ls+1):
    for j in range(1,1+lt):
        if s[i-1]==t[j-1]:
            ans[i][j] = ans[i-1][j-1]+1
        if ans[i-1][j]>ans[i][j]:
            ans[i][j]=ans[i-1][j]
        if ans[i][j-1]>ans[i][j]:
            ans[i][j]=ans[i][j-1]
i=ls
j=lt
L = []
#print(ans)
while True:
    if ans[i][j]==0:
        break
    if s[i-1]==t[j-1]:
        L.append(s[i-1])
        i-=1
        j-=1
    else:
        if ans[i][j]==ans[i][j-1]:
            j-=1
        else:
            i-=1
L.reverse()
print(*L,sep="")