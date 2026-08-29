N = int(input())
A = list(map(int,input().split()))
count = [0 for i in range(N+1)]
#両端を削り取ったら何個残っていますか？
ai_count = [0 for i in range(N)]
for i in range(N):
    count[A[i]]+=1
for i in range((N+1)//2):
    count[A[i]]-=1
    count[A[N-1-i]]-=1
    ai_count[i]=count[A[i]]
    ai_count[N-1-i]=count[A[N-1-i]]
minus = 0
#右に余白がある感じのやつ
for i in range(N//2):
    minus+=(i+1)*ai_count[i]
#左に余白がある感じのやつ
#print(minus)
for i in range((N+1)//2,N):
    minus+=(N-i)*ai_count[i]
#print(minus)
for i in range(N//2):
    if A[i]==A[N-1-i]:
        minus+=i+1
#print(minus)
plus = 0
for i in range(1,N+1):
    plus+=(i//2)*(N-i+1)
#print(plus)
print(plus-minus)


