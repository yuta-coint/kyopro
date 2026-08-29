X,Y,Z = map(int,input().split())
small_mode = 0
capital_mode = Z
S = list(input())
for ch in S:
    if ch=="a":
        cands = [small_mode+X,small_mode+2*Z+Y,capital_mode+Z+X,capital_mode+Z+Y]
        candc = [small_mode+Z+X,small_mode+Z+Y,capital_mode+Y,capital_mode+2*Z+X]
        small_mode=min(cands)
        capital_mode=min(candc)
    else:
        candc = [capital_mode+X,capital_mode+2*Z+Y,small_mode+Z+X,small_mode+Z+Y]
        cands = [capital_mode+Z+X,capital_mode+Z+Y,small_mode+Y,small_mode+2*Z+X]
        small_mode=min(cands)
        capital_mode=min(candc)
print(min(capital_mode,small_mode))