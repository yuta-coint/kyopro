T = int(input())
for case in range(T):
    N,K = map(int,input().split())
    P = [-1]+list(map(lambda x:int(x)-1,input().split()))
    G = [[] for i in range(N)]
    for i in range(1,N):
        G[P[i]].append(i)
    A = list(map(int,input().split()))
    for i in range(N):
        check = [False for i in range(K)]
        empty = 0
        stack = [i]
        flag = 0
        while stack:
            t = stack.pop()
            if A[t]==-1:
                empty+=1
            elif A[t]<K:
                check[A[t]]=True
            elif A[t]==K:
                flag=1
                break
            for u in G[t]:
                stack.append(u)
        #print(flag,empty)
        if empty>1:
            continue
        if flag==1:
            continue
        out = 0
        for j in range(K):
            if check[j]==False:
                out+=1
        if out<=1 and empty==1:
            print("Alice")
            break
        if out==0 and empty==0:
            print("Alice")
            break
    else:
        print("Bob")