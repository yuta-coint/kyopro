S = list(input())
for i in range(len(S)):
    S[i]=chr(ord(S[i])+26)
print(S,sep="")