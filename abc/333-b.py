S = input()
T = input()
grp = ["AB","BA","BC","CB","CD","DC","DE","ED","AE","EA"]
ans = 1
if S in grp:
    ans = 1-ans
if T in grp:
    ans = 1-ans
if ans==1:
    print("Yes")
else:
    print("No")