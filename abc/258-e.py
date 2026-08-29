def main():
    import sys
    input = sys.stdin.readline
    N,Q,X = map(int,input().split())
    W = list(map(int,input().split()))
    Loop = X//sum(W)
    X%=sum(W)
    sum_potatoes=[0]
    for i in range(N):
        sum_potatoes.append(sum_potatoes[i]+W[i])
    for i in range(N):
        sum_potatoes.append(sum_potatoes[N+i]+W[i])
    next = []
    cnt=0
    for i in range(N):
        while True:
            if sum_potatoes[cnt]-sum_potatoes[i]>=X:
                next.append(cnt)
                break
            cnt+=1
    temp = 0
    k = 0
    one = []
    already = set()
    while True:
        #print(temp)
        if temp in already:
            break
        one.append(temp)
        already.add(temp)
        temp = next[temp]%N
    for i in range(len(one)):
        if one[i]==temp:
            two = one[i:]
            break
    #print(next)
    #print(one)
    #print(two)
    lo = len(one)
    lt = len(two)
    for i in range(Q):
        q=int(input())
        q-=1
        if q<lo:
            print(next[one[q]]-one[q]+Loop*N)
        else:
            q-=lo
            print(next[two[q%lt]]-two[q%lt]+Loop*N)
main()