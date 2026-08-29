S = input()
last = "A"
for i in range(len(S)-1):
    if S[i]==S[i+1] or S[i]=="A" or S[i+1]=="C":
        continue
    print("No")
    exit()
print("Yes")