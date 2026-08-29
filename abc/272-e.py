N,M = map(int,input().split())
A = list(map(int,input().split()))
record = [set() for i in range(M+1)]
for i in range(N):
    start = min(max((-A[i]-1)//(i+1)+1,0),M+1)
    end = max(min((N-A[i]-1)//(i+1)+1,M+1),0)
    #print(start,end)
    for j in range(start,end):
        record[j].add((i+1)*j+A[i])
#print(record)
for i in range(1,M+1):
    for j in range(N+1):
        if j not in record[i]:
            print(j)
            break