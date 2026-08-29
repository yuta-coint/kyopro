S = input()
d = {0:3,1:2,2:4,3:1,4:3,5:5,6:0,7:2,8:4,9:6}
chk = [0 for i in range(7)]
for i in range(10):
    if S[i]=="1":
        chk[d[i]]=1
ans = "No"
chk = [0]+chk+[0]
cnt=0
for i in range(8):
    if chk[i]==0 and chk[i+1]==1:
        cnt+=1
if cnt>=2:
    ans="Yes"
if S[0]=="1":
    ans = "No"
print(ans)