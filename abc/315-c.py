N = int(input())
taste = [[] for i in range(N)]
for i in range(N):
    f,s = map(int,input().split())
    taste[f-1].append(s)
valid = []
for i in range(N):
    if len(taste[i])==0:
        continue
    elif len(taste[i])==1:
        valid.append(taste[i][0])
    else:
        taste[i].sort(reverse=True)
        valid.append(taste[i][0])
        valid.append(taste[i][1]//2)
valid.sort()
print(valid[0]+valid[1])