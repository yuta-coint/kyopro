import sys
input = sys.stdin.readline
S = input()
n = len(S)-1
back = -1
for i in reversed(range(n)):
    if S[i]!="a":
        back = i+1
        break
forth = n
for i in range(n):
    if S[i]!="a":
        forth = i
        break
if back == -1:
    print("Yes")
elif forth > n-back:
    print("No")
else:
    S = S[forth:back]
    n = len(S)
    for i in range(n):
        if S[i]!=S[n-1-i]:
            print("No")
            break
    else:
        print("Yes")