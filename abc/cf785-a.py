t = int(input())
for i in range(t):
    s = list(input())
    for i in range(len(s)):
        s[i] = ord(s[i])-ord("a")+1
    if len(s)&1:
        ans = sum(s)-min(s[0],s[-1])*2
    else:
        ans = sum(s)
    if ans>0:
        print("Alice",ans)
    else:
        print("Bob",-ans)