from collections import defaultdict
import sys
import random
input=sys.stdin.readline
N,Q = map(int,input().split())
A=[int(i) for i in input().split()]
#N=random.randrange(1,2*10**5)
#Q=random.randrange(1,2*10**5)
#print(N,Q)
#A=[random.randrange(1,2*10**5) for i in range(N)]
L=[0 for i in range(Q)]
R=[0 for i in range(Q)]
 
for i in range(Q):
    L[i],R[i]=map(int,input().split())
    L[i]-=1
def int_sqrt(n):
    low=0
    high=n+10
    while(high-low>1):
        mid=(high+low)//2
        if mid*mid<=n:
            low=mid
        else:
            high=mid
    return low
Qsqrt=int_sqrt(Q)
B=1+N//Qsqrt
query=[((L[i]//B)<<40)+((R[i] if (L[i]//B)&1 else -R[i])<<20)+i for i in range(Q)]
query.sort()
geta=(1<<20)-1
l=0
r=0
nowans=0
nowdict=[0 for i in range(200001)]
ans=[0 for i in range(Q)]
for j in range(Q):
    nidx=query[j]&geta
    nl=L[nidx]
    nr=R[nidx]
    while(l<nl):
        nowdict[A[l]]-=1
        nowans-=nowdict[A[l]]*(nowdict[A[l]]-1)//2
        l+=1
    while(l>nl):
        nowans+=nowdict[A[l-1]]*(nowdict[A[l-1]]-1)//2
        nowdict[A[l-1]]+=1
        l-=1
    while(r<nr):
        nowans+=nowdict[A[r]]*(nowdict[A[r]]-1)//2
        nowdict[A[r]]+=1
        r+=1
    while(r>nr):
        nowdict[A[r-1]]-=1
        nowans-=nowdict[A[r-1]]*(nowdict[A[r-1]]-1)//2
        r-=1
    ans[nidx]=nowans
print(*ans,sep="\n")