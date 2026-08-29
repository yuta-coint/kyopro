N = int(input())
S = input()
for i in range(N):
    if (i&1 and S[i]==S[0]) or (i%2==0 and S[i]!=S[0]):
        print("No")
        break
else:
    print("Yes")
