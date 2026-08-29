s = input()
l = len(s)
a = l//2
center = s[l//2]
while a<l:
    if s[a]==center and s[l-1-a]==center:
        a+=1
    else:
        break
print(a)