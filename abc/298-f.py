import sys
input  =sys.stdin.readline
def coordinate_compression(A):
    b = sorted(set(A))
    d ={v:i for i, v in enumerate(b)}
    return list(map(lambda v:d[v],A))
N = int(input())
R = []
C = []
X = []
for i in range(N):
    r,c,x = map(int,input().split())
    R.append(r)
    C.append(c)
    X.append(x)
R = coordinate_compression(R)
C = coordinate_compression(C)
points = [R[i]*(10**9)+C[i] for i in range(N)]
points = {points[i]:X[i] for i in range(N)}
r_sum = [0 for i in range(2*(10**5)+3)]
c_sum = [0 for i in range(2*(10**5)+3)]
for i in range(N):
    r_sum[R[i]]+=X[i]
    c_sum[C[i]]+=X[i]
r_sum2= [(r_sum[i],i) for i in range(2*(10**5)+3)]
r_sum2.sort(reverse=True)
r_sum2 = [r_sum2[i][1] for i in range(2*(10**5)+3)]
check_c = set()
ans = 0
for i in range(N):
    if C[i] in check_c:
        continue
    check_c.add(C[i])
    for j in range(2*(10**5)+3):
        rr = r_sum2[j]
        p = rr*(10**9)+C[i]
        if p in points:
            if r_sum[rr]+c_sum[C[i]]-points[p]>ans:
                ans = r_sum[rr]+c_sum[C[i]]-points[p]
        else:
            if r_sum[rr]+c_sum[C[i]]>ans:
                ans = r_sum[rr]+c_sum[C[i]]
            break
print(ans)