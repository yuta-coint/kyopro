import sys
N = int(input())
ssf = sys.stdout.flush
def ins(k):
    m = 0
    M = len(arr)+1
    while m+1<M:
        mid = (m+M)//2
        print("?",arr[mid-1],k)
        ssf()
        Q = int(input())
        if Q == 1:
            m = mid
        else:
            M = mid
    arr.insert(m,k)
#from array import array
arr = [1]
for i in range(2,N+1):
    ins(i)
print("+",arr[0],arr[-1])
ssf()
p = arr[0]
arr.pop()
arr.pop(0)
P = int(input())
while P<2*N-1:
    ins(P)
    print("+",arr[0],arr[-1])
    ssf()
    arr.pop()
    arr.pop(0)
    P = int(input())
print("!")