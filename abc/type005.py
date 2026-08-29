def main():
    N,B,K = map(int,input().split())
    pow10 = [1]
    setp = set(pow10)
    cnt = 1
    while True:
        cnt*=10
        cnt%=B
        if cnt in setp:
            cut = pow10.index(cnt)
            powloop = pow10[cut:]
            break
        pow10.append(cnt)
        setp.add(cnt)
    loop = len(powloop)
    if N>cut:
        powrem = pow10[:cut+(N-cut)%loop]
    else:
        powrem = pow10[:N]
    mod = 10**9+7
    c = list(map(int,input().split()))
    #n=bのときの答え
    patb = [0 for i in range(B)]
    patb[0]=1
    for i in range(len(powrem)):
        temp = [0 for _ in range(B)]
        for ci in c:
            for j in range(B):
                temp[j]+=patb[(j-ci*powrem[i])%B]
                temp[j]%=mod
        patb = temp
    patL = [0 for i in range(B)]
    patL[0]=1
    for i in range(loop):
        temp = [0 for _ in range(B)]
        for ci in c:
            for j in range(B):
                temp[j]+=patL[(j-ci*powloop[i])%B]
                temp[j]%=mod
        patL = temp
    #とりあえずNをphibでわった商の分だけ行列を掛ける
    time = (N-len(powrem))//loop
    matans = [0 for i in range(B)]
    matans[0]=1
    for i in reversed(range(len(bin(time))-2)):
        temp = [0 for _ in range(B)]
        for r in range(B):
            for f in range(B):
                temp[(r+f)%B]+=matans[r]*matans[f]%mod
                temp[(r+f)%B]%=mod
        matans = temp
        if time>>i & 1:
            temp = [0 for _ in range(B)]
            for r in range(B):
                for f in range(B):
                    temp[(r+f)%B]+=matans[r]*patL[f]%mod
                    temp[(r+f)%B]%=mod
            matans = temp
    ans = [0 for i in range(B)]
    #print(matans)
    for r in range(B):
        for f in range(B):
            ans[(r+f)%B]+=matans[r]*patb[f]
            ans[(r+f)%B]%=mod
    print(ans[0])
main()