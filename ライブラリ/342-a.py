S =  list(input())
if S[0]!=S[1]:
    if S[0]!=S[2]:
        print(1)
    else:
        print(2)
else:
    for i in range(2,len(S)):
        if S[i]!=S[0]:
            print(i+1)