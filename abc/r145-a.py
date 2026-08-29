N = int(input())
S = input()
if S[0]=="A" and S[-1]=="B":
    print("No")
elif N==2 and S[0]=="B" and S[-1]=="A":
    print("No")
else:
    print("Yes")