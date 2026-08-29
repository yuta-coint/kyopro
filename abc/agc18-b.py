n,m = map(int,input().split())
import sys
input = sys.stdin.readline
point = []
a = []
for i in range(n):
    ai = list(map(lambda x:int(x)-1,input().split()))
    a.append(ai)
ban = set()
#各選手が第何希望を選ぶか
ans = n
choice = [0 for i in range(n)]
for _ in range(m):
    #print(choice)
    #人気種目の封鎖
    cnt2 = [0 for i in range(m)]
    for i in range(n):
        cnt2[a[i][choice[i]]]+=1
    ans = min(ans,max(cnt2))
    ban.add(cnt2.index(max(cnt2)))
    if _==m-1:
        break
    #種目の更新
    for i in range(n):
        while a[i][choice[i]] in ban:
            choice[i]+=1
print(ans)