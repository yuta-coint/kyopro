def Misere_Nim(S):
    xor_S = 0
    for i in range(len(S)):
        xor_S ^= S[i]
    if (max(S) == 1) and (xor_S == 1):
        return False
    if (max(S) > 1) and (xor_S == 0):
        return False
    return True

N = int(input())
A = list(map(int,input().split()))
grundy = 0
for i in range(N):
    grundy ^= A[i]
if grundy == 1:
    print("Bob")
else:
    print("Alice")