N = int(input())
S = list(input())
T  =list(input())
if sorted(S)!=sorted(T):
    print(-1)
    exit()
key = N-1
for i in reversed(range(N)):
    if T[i]==S[key]:
        key-=1
print(key+1)