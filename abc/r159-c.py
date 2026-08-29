from copy import copy
N = int(input())
a = list(map(int,input().split()))
test = copy(a)
if N&1:
    if sum(a)%N>0:
        print("No")
        exit()
else:
    if sum(a)%(N//2)>0:
        print("No")
        exit()
#sを-k,tを+kする
ans = []
if sum(a)%N>0:
    ans.append([i+1 for i in range(N)])
    for i in range(N):
        a[i]+=i+1
if sum(a)%N>0:
    print("No")
    exit()
print("Yes")
def game(s,t,k):
    cnt = 1
    p = []
    for i in range(N):
        if i==s:
            p.append(0)
        elif i==t:
            p.append(k)
        else:
            if cnt==k:
                cnt+=1
            p.append(cnt)
            cnt+=1
    for i in range(N):
        p[i]+=1
    ans.append(p)
    for i in range(1,N):
        p = []
        cnt=(i+1)%N
        for j in range(N):
            if j==t:
                p.append(i)
            elif j==s:
                p.append((k+i)%N)
            else:
                if cnt==(k+i)%N:
                    cnt+=1
                    if cnt==N:
                        cnt-=N
                p.append(cnt)
                cnt+=1
                if cnt==N:
                    cnt-=N
        for j in range(N):
            p[j]+=1
        ans.append(p)
    a[s]-=k
    a[t]+=k
def plus_N(s):
    temp = [i for i in range(1,N)]
    p = temp[:s]+[N]+temp[s:]
    ans.append(p)
    temp = [N-i for i in range(1,N)]
    p = temp[:s]+[N]+temp[s:]
    ans.append(p)
    a[s]+=N
def minus_N(s):
    temp = [i+1 for i in range(1,N)]
    p = temp[:s]+[1]+temp[s:]
    ans.append(p)
    temp = [N-i+1 for i in range(1,N)]
    p = temp[:s]+[1]+temp[s:]
    ans.append(p)
    a[s]-=N
tar = max(a)
for i in range(N):
    for _ in range((tar-a[i])//N):
        plus_N(i)
ave = sum(a)//N
#print(a)
for i in range(N):
    a[i]-=ave
for i in range(N):
    ma = a.index(max(a))
    mi = a.index(min(a))
    if a[ma]==0:
        break
    game(ma,mi,-a[mi])
print(len(ans))
for p in ans:
    print(*p)
for p in ans:
    for i in range(N):
        test[i]+=p[i]
print(test)