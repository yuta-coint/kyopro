N = int(input())
S = list(input())
Q = int(input())
no_change = set()
letter = 0
for i in range(Q):
    t,x,c = input().split()
    t = int(t)
    x = int(x)
    if t==1:
        S[x-1]=c
        no_change.add(x-1)
    elif t==2:
        letter = 1
        no_change = set()
    else:
        letter = -1
        no_change = set()
print(*S)
for i in range(N):
    if i in no_change:
        continue
    if 0<=ord(S[i])-ord("a")<26 and letter==-1:
        S[i]=chr(ord(S[i])-ord("a")+ord("A"))
    elif 0<=ord(S[i])-ord("A")<26 and letter==1:
        S[i]=chr(ord(S[i])+ord("a")-ord("A"))
print(*S,sep="")
