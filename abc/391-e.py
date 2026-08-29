N = int(input())
A = list(input())
for i in range(3**N):
    A[i] = int(A[i])
#今のスコアを確かめる。
B = A
hiaerarchy = [A]
for t in reversed(range(N)):
    next_hia = []
    for i in range(3**t):
        if hiaerarchy[-1][3*i]+hiaerarchy[-1][3*i+1]+hiaerarchy[-1][3*i+2]>=2:
            next_hia.append(1)
        else:
            next_hia.append(0)
    hiaerarchy.append(next_hia)
if hiaerarchy[-1][0]==0:
    for i in range(3**N):
        A[i] = 1-A[i]
norma = [A]
for t in reversed(range(N)):
    #一つ下の階層から一番大きいのを除いてとる。
    next_norma = []
    for i in range(3**t):
        next_norma.append(norma[-1][3*i]+norma[-1][3*i+1]+norma[-1][3*i+2]-max(norma[-1][3*i],norma[-1][3*i+1],norma[-1][3*i+2]))
    norma.append(next_norma)
print(norma[-1][0])