N = int(input())
S = list(input())
nexto = []
nextx = []
tempo = N
tempx = N
for i in reversed(range(N)):
    if S[i]=="o":
        tempo = i
    else:
        tempx = i
    nexto.append(tempo)
    nextx.append(tempx)
nexto.reverse()
nextx.reverse()
ans = 0
for i in range(N):
    if S[i]=="o":
        ans+=N-nextx[i]
    else:
        ans+=N-nexto[i]
print(ans)


