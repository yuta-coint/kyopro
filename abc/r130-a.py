n = int(input())
s = input()
last = s[0]
ans = 0
store = 0
for i in range(1,n):
    if s[i]==last:
        store+=1
    else:
        store=0
    ans += store
    last = s[i]
print(ans)
