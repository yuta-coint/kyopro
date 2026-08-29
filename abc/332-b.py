K,G,M  = map(int,input().split())
glass = 0
mug = 0
for i in range(K):
    if glass==G:
        glass = 0
    elif mug == 0:
        mug = M
    elif glass+mug<=G:
        glass+=mug
        mug = 0
    else:
        mug = mug+glass-G
        glass = G
print(glass,mug)