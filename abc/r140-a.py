N,k = map(int,input().split())
s = input()
for ans in range(1,N+1):
    if N%ans!=0:
        continue
    cnt = [[0 for j in range(26)] for i in range(ans)]
    for i in range(N):
        cnt[(i%ans)][(ord(s[i])-ord("A"))%26]+=1
    mani=0
    for i in range(ans):
        mani += (N//ans)-max(cnt[i])
    #print(mani)
    if mani<=k:
        print(ans)
        break
else:
    print(N)