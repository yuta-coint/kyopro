import itertools
N,B = map(int,input().split())
ans = 0
def keta_part(N):
    r = []
    while N>0:
        r.append(N%10)
        N//=10
    r.sort()
    return(tuple(r))
for keta in range(1,12):
    for digits in(itertools.combinations_with_replacement(range(1,10),keta)):
        fm = 1
        for d in digits:
            fm*=d
        m = fm+B
        if m>N:
            continue
        if digits == keta_part(m):
            ans+=1
#0が入っている,、すなわちm=Bのパターン
if 0 in keta_part(B) and B<=N:
    ans+=1
print(ans)