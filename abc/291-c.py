N=int(input())
S = input()
temp = 0
visited = set()
big = 10**7
visited.add(0)
for i in range(N):
    if S[i]=="R":
        temp+=1
    elif S[i]=="L":
        temp-=1
    elif S[i]=="U":
        temp+=big
    else:
        temp-=big
    if temp in visited:
        print("Yes")
        exit()
    visited.add(temp)
print("No")