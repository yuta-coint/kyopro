def main():
    N = int(input())
    #平方因子
    sq  =[1 for i in range(N+1)]
    from math import gcd
    for i in range(2,10**3):
        #print((N//(i*i))+1)
        for j in range(1,(N//(i*i))+1):
            sq[i*i*j]=(sq[i*i*j]*i*i)//gcd(sq[i*i*j],i*i)
    #print(sq)
    ans = 0
    for i in range(1,N+1):
        a = i//sq[i]
        ans+=int((N//a)**(1/2))
        #print(ans)
    #print(ans)
main()