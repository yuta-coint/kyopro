N,K = map(int,input().split())
A = list(map(int,input().split()))
d = {}
mac = 1
for i in range(N):
    if A[i] in d:
        d[A[i]]+=1
        if d[A[i]]>mac:
            mac = d[A[i]]
    else:
        d[A[i]]=1
cand = []
for ind in d:
    if d[ind]==mac:
        cand.append(ind)
cand.sort()
T = 0
for i in range(len(cand)-1):
    if cand[i+1]-cand[i]>T:
        T = cand[i+1]-cand[i]
if K+cand[0]-cand[-1]>T:
    T = K+cand[0]-cand[-1]
print(-(K-T)+(N-mac)*K)