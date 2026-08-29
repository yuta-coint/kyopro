ache = [0]
heal = [0]
N = int(input())
for i in range(N):
    x,y=map(int,input().split())
    if x==0:
        heal.append(max([heal[i],heal[i]+y,ache[i]+y]))
        ache.append(ache[i])
    else:
        heal.append(heal[i])
        ache.append(max(ache[i],heal[i]+y))
print(max(heal[-1],ache[-1]))