def main():
    N = int(input())
    S = list(input())
    mod = 998244353
    dp = [0 for i in range(26*26)]
    if S[0]=="?" and S[1]=="?":
        for i in range(26):
            for j in range(26):
                if i==j:
                    continue
                dp[i*26+j]=1
    elif S[1]=="?":
        for i in range(26):
            if i==ord(S[0])-ord("a"):
                continue
            dp[i*26+ord(S[0])-ord("a")]=1
    elif S[0]=="?":
        for j in range(26):
            if j==ord(S[1])-ord("a"):
                continue
            dp[(ord(S[1])-ord("a"))*26+j]=1
    else:
        if S[0]!=S[1]:
            dp[(ord(S[1])-ord("a"))*26+ord(S[0])-ord("a")]=1
    for i in range(2,N):
        new = [0 for i in range(26*26)]
        #print(S[i])
        if S[i]=="?":
            for i in range(26):
                for j in range(26):
                    if i==j:
                        continue
                    for k in range(26):
                        if k==i or k==j:
                            continue
                        new[k*26+j]+=dp[j*26+i]
                        if new[k*26+j]>=mod:
                            new[k*26+j]-=mod
        else:
            k = ord(S[i])-ord("a")
            for i in range(26):
                for j in range(26):
                    if k==i or k==j:
                        continue
                    new[k*26+j]+=dp[j*26+i]
                    if new[k*26+j]>=mod:
                        new[k*26+j]-=mod
        dp = new
    ans = 0
    for i in range(26*26):
        ans+=dp[i]
        if ans>=mod:
            ans-=mod
    print(ans)
main()