N,Q = map(int,input().split())
queries = []
a = [0,N]
for i in range(Q):
    l,r = map(int,input().split())
    queries.append((l-1,r))
    a.append(l-1)
    a.append(r)
b = sorted(set(a))
d = {v:i for i, v in enumerate(b)}
#aの要素に対して「vに対してd[v]を返す」
for i in range(Q):
    queries[i] = (d[queries[i][0]],d[queries[i][1]])
d = len(bin(len(b)-1))-2
