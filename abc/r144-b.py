def main():
    N,a,b = map(int,input().split())
    A = list(map(int,input().split()))
    m = 0
    M = 10**9+1
    while m+1<M:
        temp = (m+M)//2
        life = 0
        damage = 0
        for i in range(N):
            if A[i]>=temp:
                life+=(A[i]-temp)//b
            else:
                damage-=(A[i]-temp)//a
        if damage>life:
            M=temp
        else:
            m=temp
    print(m)
main()