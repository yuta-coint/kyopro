N = int(input())
ans = []
for i in range(1,2**N):
    cnt = 0
    while True:
        if (i>>cnt)&1:
            cnt+=1
            break
        else:
            cnt+=1
    ans.append(cnt)
print(*ans)


N = int(input())
ind = []
ans = "Yes"
name = [list(input().split()) for i in range(N)]
sname = []
for i in range(N):
    fa,fi = name[i][0],name[i][1]
    sname.append(fa)
    sname.append(fi)
sname2 = set(sname)
cnt = {i:0 for i in sname2}
for i in range(N):
    fa,fi = name[i][0],name[i][1]
    cnt[fa]+=1
    if fa!=fi:
        cnt[fi]+=1
for i in range(N):
    fa,fi = name[i][0],name[i][1]
    if cnt[fa]>=2 and cnt[fi]>=2:
        ans = "No"
print(ans)

s = input()
print("0"+s[:-1])
    

