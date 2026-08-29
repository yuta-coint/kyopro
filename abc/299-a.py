N = int(input())
S = input()
a = -1
b = -1
c = -1
for i in range(N):
    if S[i]=="|":
        if a==-1:
            a=i
        else:
            c=i
    elif S[i]=="*":
        b = i
if a<b and b<c:
    print("in")
else:
    print("out")