N = int(input())
T=input()
A=input()
ans = "No"
for i in range(N):
    if T[i] == "o" and A[i]=="o":
        ans = "Yes"
print(ans)