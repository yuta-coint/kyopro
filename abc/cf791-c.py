import sys
input = sys.stdin.readline
#RSQ
#RMQ
def main():
    N,q = map(int,input().split())
    N+=1
    c = 1
    n = 1
    while c<N:
        c*=2
        n+=1
    SEGx = [0 for i in range(2**n)]#n段のセグ木
    def updatex(i,a):
        i += 2**(n-1)
        SEGx[i]=a
        while i>1:
            i //= 2
            SEGx[i] = min(SEGx[2*i],SEGx[2*i+1])
    def findx(s,t):
        k = 1
        s += 2**(n-1)
        t += 2**(n-1)
        while s<=t:
            if s%2==1:
                k = min(k,SEGx[s])
                s//=2
                s+=1
            else:
                s//=2
            if t%2==0:
                k = min(k,SEGx[t])
                t//=2
                t-=1
            else:
                t//=2
        return(k)
    #RMQ
    SEGy = [0 for i in range(2**n)]#n段のセグ木
    def updatey(i,a):
        i += 2**(n-1)
        SEGy[i]=a
        while i>1:
            i //= 2
            SEGy[i] = min(SEGy[2*i],SEGy[2*i+1])
    def findy(s,t):
        k = 1
        s += 2**(n-1)
        t += 2**(n-1)
        while s<=t:
            if s%2==1:
                k = min(k,SEGy[s])
                s//=2
                s+=1
            else:
                s//=2
            if t%2==0:
                k = min(k,SEGy[t])
                t//=2
                t-=1
            else:
                t//=2
        return(k)
    for _ in range(q):
        t = list(map(int,input().split()))
        #print(findx(t[1],t[1]),findx(t[2],t[2]))
        if t[0]==1:
            updatex(t[1],SEGx[t[1]+2**(n-1)]+1)
            updatey(t[2],SEGy[t[2]+2**(n-1)]+1)
        elif t[0]==2:
            updatex(t[1],SEGx[t[1]+2**(n-1)]-1)
            updatey(t[2],SEGy[t[2]+2**(n-1)]-1)
        else:
            #print(findx(t[1],t[3]),findy(t[2],t[4]))
            if findx(t[1],t[3])==0 and findy(t[2],t[4])==0:
                print("No")
            else:
                print("Yes")
main()

