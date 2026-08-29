S = input()
ans = 0
now = 0
mae = [0 for i in range(26)]
usiro = [0 for i in range(26)]
for i in range(len(S)):
    usiro[ord(S[i])-ord("A")]+=1
for i in range(len(S)):
    t = ord(S[i])-ord("A")
    now-=mae[t]*usiro[t]
    usiro[t]-=1
    now+=mae[t]*usiro[t]
    ans+=now
    now-=mae[t]*usiro[t]
    mae[t]+=1
    now+=mae[t]*usiro[t]
print(ans)