S = list(input().split())
T = list(input().split())
ans = "No"
if S == T:
    ans = "Yes"
S[0],S[1]=S[1],S[0]
S[2],S[1]=S[1],S[2]
if S == T:
    ans = "Yes"
S[0],S[1]=S[1],S[0]
S[2],S[1]=S[1],S[2]
if S == T:
    ans = "Yes"
print(ans)
