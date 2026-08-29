S = input()
T= input()
if S==T:
    print(0)
    exit()
for i in range(min(len(S),len(T))):
    if S[i]!=T[i]:
        print(i+1)
        exit()
print(min(len(S),len(T))+1)