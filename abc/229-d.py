s = input()
k = int(input())
cnt = 0
sl = [0]
for i in range(len(s)):
    if s[i]==".":
        cnt+=1
    sl.append(cnt)
r = 0
l = 0
ans =0
while r<=len(s):
    if sl[r]-sl[l]<=k:
        ans = max(ans,r-l)
        r+=1
    else:
        l+=1
print(ans)