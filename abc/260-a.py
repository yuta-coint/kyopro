S = input()
if S[1]!=S[0] and S[2]!=S[0]:
    print(S[0])
elif S[1]!=S[0] and S[2]!=S[1]:
    print(S[1])
elif S[1]!=S[2] and S[2]!=S[0]:
    print(S[2])
else:
    print(-1)