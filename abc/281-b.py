S = input()
if len(S)!=8:
    print("No")
    exit()
ch = []
for i in range(8):
    if 0<=ord(S[i])-ord("A")<26:
        ch.append(i)
if ch==[0,7] and int(S[1])>0:
    print("Yes")
else:
    print("No")

