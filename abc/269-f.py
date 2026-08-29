import sys
input = sys.stdin.readline
N,M = map(int,input().split())
Q = int(input())
mod = 998244353
half = 499122177
for i in range(Q):
    A,B,C,D = map(int,input().split())
    temp = (((B-1)*B-(A-2)*(A-1))%mod*half%mod*M%mod*(D-C+1)%mod+(D*(D+1)-(C-1)*C)%mod*499122177%mod*(B-A+1)%mod)%mod
    #print(temp)
    if ((B-A)&1) and ((D-C)&1):
        print(temp*half%mod)
    elif ((B-A)&1) and (A+C)&1:
        print((temp+((B-A+1)>>1)*M%mod)%mod*half%mod)
    elif ((B-A)&1):
        print((temp-((B-A+1)>>1)*M%mod)%mod*half%mod)
    elif ((D-C)&1) and (A+C)&1:
        print((temp+((D-C+1)>>1)%mod)%mod*half%mod)
    elif ((D-C)&1):
        #print(372)
        print((temp-((D-C+1)>>1)%mod)%mod*half%mod)
    else:
        temp*=pow((B-A+1)*(D-C+1)%mod,mod-2,mod)
        temp%=mod
        if (A+C)&1:
            temp*=((B-A+1)*(D-C+1)%mod-1)*half%mod
            print(temp%mod)
        else:
            temp*=((B-A+1)*(D-C+1)%mod+1)*half%mod
            print(temp%mod)