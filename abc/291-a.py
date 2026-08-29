S = input()
for i in range(len(S)):
    if 0<=ord(S[i])-ord("a")<26:
        continue
    print(i+1)
    exit()