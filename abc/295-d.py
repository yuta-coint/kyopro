S = list(input())
sum_h = [0]
for i in range(len(S)):
    sum_h.append(sum_h[-1]^(1<<int(S[i])))
count = {}
ans = 0
for p in sum_h:
    if p in count:
        ans+=count[p]
        count[p]+=1
    else:
        count[p]=1
print(ans)