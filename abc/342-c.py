n=26
label = [chr(ord("a")+i) for i in range(n)]

N = int(input())
S = list(input())
Q = int(input())

for qe in range(Q):
    c,d = input().split()
    for i in range(26):
        if label[i]==c:
            label[i]=d
#print(label)
for i in range(len(S)):
    S[i] = label[ord(S[i])-ord("a")]
print(*S,sep="")