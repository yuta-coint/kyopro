N = int(input())
S = input()
one = []
for i in range(N):
    if S[i]=="1":
        one.append(i)
for i in range(len(one)):
    one[i]-=i
med = one[len(one)//2]
ans = 0
for x in one:
    ans += abs(med-x)
print(ans)
    