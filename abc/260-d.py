def main():
    from array import array
    import bisect
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    field = array('i',[-1])
    cnt = array('i',[-1])
    over = [0 for i in range(N+1)]
    ans = [-1 for i in range(N+1)]
    if K!=1:
        for i in range(N):
            if field[-1]<P[i]:
                field.append(P[i])
                cnt.append(1)
            else:
                b = bisect.bisect(field,P[i])
                over[P[i]]=field[b]
                field[b]=P[i]
                cnt[b]+=1
                if cnt[b]==K:
                    p = P[i]
                    for j in range(K):
                        ans[p]=i+1
                        p=over[p]
                    field.pop(b)
                    cnt.pop(b)
    else:
        for i in range(N):
            ans[P[i]]=i+1
    for i in range(1,N+1):
        print(ans[i])
main()





