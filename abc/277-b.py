N = int(input())
one = ["H","D","C","S"]
two = ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]
already = set()
ans = "Yes"
for i in range(N):
    S = input()
    if S[0] in one and S[1] in two and (not (S in already)):
        already.add(S)
    else:
        ans = "No"
print(ans)
