N,M = map(int,input().split())
A = list(map(int,input().split()))
cnt = {}
for i in range(2*N):
    if A[i] in cnt:
        cnt[A[i]]+=1
    else:
        cnt[A[i]]=1
single = []
for i in cnt:
    if cnt[i]&1:
        single.append(i)
#print(single)
if len(single) == 0:
    print("Bob")
elif M&1:
    print("Alice")
elif len(single)%4==2:
    print("Alice")
else:
    ss = set(single)
    hm = M//2
    for i in single:
        if not ((i+hm)%M in ss):
            print("Alice")
            break
    else:
        print("Bob")
