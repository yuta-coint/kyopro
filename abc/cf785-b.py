t = int(input())
for i in range(t):
    s = list(input())
    chk = [-1 for i in range(26)]
    loop = 0
    ans = "YES"
    c = -1
    ls = set()
    for i in range(len(s)):
        t = ord(s[i])-ord("a")
        ls.add(t)
    t = len(ls)
    for i in range(t,len(s)):
        if s[i]!=s[i-t]:
            ans = "NO"
    print(ans)
