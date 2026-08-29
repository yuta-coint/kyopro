N = int(input())
S = list(input())+["0"]
ans = []
for i in reversed(range(N)):
    if S[i]=="0" and S[i+1]=="1":
        for j in range(i+1):
            ans.append("B")
    elif S[i]=="1" and S[i+1]=="0":
        for j in range(i+1):
            ans.append("A")
print(len(ans))
print(ans,sep="")